from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from functools import wraps
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
app.config['SESSION_COOKIE_DURATION'] = timedelta(minutes=5)

def get_db_connection():
    conn = sqlite3.connect('gestao_hospitalar.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Criação de tabelas
conn = get_db_connection()
cursor = conn.cursor()
cursor.executescript('''
    CREATE TABLE IF NOT EXISTS USUARIO (
        NM_USUARIO TEXT PRIMARY KEY,
        DS_USUARIO TEXT,
        DS_SENHA TEXT NOT NULL,
        TIPO_USUARIO TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS CONSULTA (
        ID_CONSULTA INTEGER PRIMARY KEY AUTOINCREMENT,
        NM_PACIENTE TEXT NOT NULL,
        MEDICO TEXT NOT NULL,
        ESPECIALIDADE TEXT NOT NULL,
        DATA TEXT NOT NULL,
        HORARIO TEXT NOT NULL,
        STATUS TEXT DEFAULT 'Agendado'
    );
    CREATE TABLE IF NOT EXISTS PRONTUARIO (
        ID_PRONTUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
        NM_PACIENTE TEXT NOT NULL,
        HISTORICO TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS EXAME (
        ID_EXAME INTEGER PRIMARY KEY AUTOINCREMENT,
        NM_PACIENTE TEXT NOT NULL,
        TIPO_EXAME TEXT NOT NULL,
        DATA TEXT NOT NULL,
        RESULTADO TEXT
    );
''')
conn.commit()
conn.close()


# Decorador de autenticação
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            flash('Você precisa estar logado para acessar esta página.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nm_usuario = request.form['NM_USUARIO']
        senha = request.form['DS_SENHA']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DS_SENHA, TIPO_USUARIO FROM USUARIO WHERE NM_USUARIO = ?", (nm_usuario,))
        usuario = cursor.fetchone()
        conn.close()

        if usuario and check_password_hash(usuario['DS_SENHA'], senha):
            session['usuario'] = nm_usuario
            session['tipo_usuario'] = usuario['TIPO_USUARIO']  # Armazenar o tipo do usuário na sessão
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuário ou senha incorretos.', 'danger')
    return render_template('login.html')


@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
@login_required
def cadastrar_usuario():
    if session.get('tipo_usuario') not in ['admin']:  # Apenas admins podem cadastrar usuários
        flash('Apenas administradores podem cadastrar usuários.', 'warning')
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Pegar os dados do formulário
        nm_usuario = request.form['usuario']
        ds_senha = generate_password_hash(request.form['senha'])
        tipo_usuario = request.form['tipo']  # tipo pode ser 'medico', 'enfermeiro', 'recepcionista', 'admin'

        # Verificar se o usuário já existe
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USUARIO WHERE NM_USUARIO = ?", (nm_usuario,))
        usuario = cursor.fetchone()
        
        if usuario:
            flash('Usuário já existe!', 'danger')
            conn.close()
            return redirect(url_for('cadastrar_usuario'))

        # Cadastrar o novo usuário
        cursor.execute("INSERT INTO USUARIO (NM_USUARIO, DS_USUARIO, DS_SENHA, TIPO_USUARIO) VALUES (?, ?, ?, ?)", 
                       (nm_usuario, nm_usuario, ds_senha, tipo_usuario))
        conn.commit()
        conn.close()

        flash('Usuário cadastrado com sucesso!', 'success')
        return redirect(url_for('home'))

    return render_template('cadastrar_usuario.html')

@app.route('/atualizar_usuario/<string:nm_usuario>', methods=['GET', 'POST'])
@login_required
def atualizar_usuario(nm_usuario):
    if session.get('tipo_usuario') not in ['admin'] and session.get('usuario') != nm_usuario:
        flash('Você não tem permissão para atualizar este usuário.', 'warning')
        return redirect(url_for('home'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USUARIO WHERE NM_USUARIO = ?", (nm_usuario,))
    usuario = cursor.fetchone()

    if request.method == 'POST':
        # Atualizando os dados do usuário
        nova_senha = request.form['senha']
        tipo_usuario = request.form['tipo']  # Novo tipo de usuário

        # Atualizar a senha, se fornecida
        if nova_senha:
            nova_senha_hash = generate_password_hash(nova_senha)
            cursor.execute("UPDATE USUARIO SET DS_SENHA = ?, TIPO_USUARIO = ? WHERE NM_USUARIO = ?", 
                           (nova_senha_hash, tipo_usuario, nm_usuario))
        else:
            cursor.execute("UPDATE USUARIO SET TIPO_USUARIO = ? WHERE NM_USUARIO = ?", 
                           (tipo_usuario, nm_usuario))

        conn.commit()
        conn.close()
        flash('Usuário atualizado com sucesso!', 'success')
        return redirect(url_for('home'))

    return render_template('atualizar_usuario.html', usuario=usuario)

@app.route('/agendar_consulta', methods=['GET', 'POST'])
@login_required
def agendar_cancelar_consulta():
    if request.method == 'POST':
        # Caso o formulário de agendamento seja enviado
        if 'paciente' in request.form:  # Verifica se o campo 'paciente' foi enviado
            paciente = request.form['paciente']
            medico = request.form['medico']
            especialidade = request.form['especialidade']
            data = request.form['data']
            horario = request.form['horario']

            # Inserir a consulta no banco de dados
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO CONSULTA (NM_PACIENTE, MEDICO, ESPECIALIDADE, DATA, HORARIO) VALUES (?, ?, ?, ?, ?)", 
                           (paciente, medico, especialidade, data, horario))
            conn.commit()
            conn.close()
            flash('Consulta agendada com sucesso!', 'success')

        # Caso o formulário de cancelamento seja enviado
        elif 'consulta_id' in request.form:  # Verifica se o campo 'consulta_id' foi enviado
            consulta_id = request.form['consulta_id']

            # Atualizar o status da consulta para "Cancelado"
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE CONSULTA SET STATUS = 'Cancelado' WHERE ID_CONSULTA = ?", (consulta_id,))
            conn.commit()
            conn.close()
            flash('Consulta cancelada com sucesso!', 'info')

        return redirect(url_for('agendar_cancelar_consulta'))

    return render_template('agendar_consulta.html')

@app.route('/cancelar_consulta/<int:id>', methods=['POST'])
@login_required
def cancelar_consulta(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE CONSULTA SET STATUS = 'Cancelado' WHERE ID_CONSULTA = ?", (id,))
    conn.commit()
    conn.close()
    flash('Consulta cancelada.', 'info')
    return redirect(url_for('home'))

@app.route('/checkin/<int:id>', methods=['POST'])
@login_required
def checkin(id):
    # Verificar se o usuário tem permissões de recepcionista (opcional)
    if session.get('tipo_usuario') not in ['recepcionista', 'admin']:
        flash('Apenas recepcionistas e administradores podem realizar o check-in.', 'warning')
        return redirect(url_for('home'))
    
    # Atualizar o status da consulta para "Check-in Realizado"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE CONSULTA SET STATUS = 'Check-in Realizado' WHERE ID_CONSULTA = ?", (id,))
    conn.commit()
    conn.close()

    flash('Check-in realizado com sucesso!', 'success')
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
