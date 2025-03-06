from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from functools import wraps
import sqlite3

app = Flask(__name__)
# Chave que habilita o uso de sessões pelo Flask, e assina os cookies das sessões
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
# Encerra a sessão do usuário caso ele fique inativo pelo tempo determinado
app.config['SESSION_COOKIE_DURATION'] = timedelta(minutes=5)

# Cria as tabelas se não existirem
conn = sqlite3.connect('gestao_hospitalar.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS USUARIO (
        NM_USUARIO TEXT PRIMARY KEY,
        DS_USUARIO TEXT,
        DS_SENHA TEXT NOT NULL
    )
    '''
)
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS PERFIL (
    ID_PERFIL INTEGER PRIMARY KEY AUTOINCREMENT,
    DS_PERFIL TEXT NOT NULL
    )
    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS USUARIO_PERFIL (
    NM_USUARIO TEXT,
    ID_PERFIL INTEGER,
    FOREIGN KEY (NM_USUARIO) REFERENCES USUARIO (NM_USUARIO),
    FOREIGN KEY (ID_PERFIL) REFERENCES PERFIL (ID_PERFIL),
    PRIMARY KEY (NM_USUARIO, ID_PERFIL)
    )
    '''
)
conn.commit()
conn.close()

# Define um decorador para dizer as rotas se é necessário ou não estar logado para acessar aquela página
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            flash('Você não está logado! Faça login para acessar o sistema.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nm_usuario = request.form['NM_USUARIO']
        senha = request.form['DS_SENHA']
        
        # Conectar ao banco e buscar usuário
        conn = sqlite3.connect('gestao_hospitalar.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("SELECT DS_SENHA FROM USUARIO WHERE NM_USUARIO = ?", (nm_usuario,))
        usuario = cursor.fetchone()
        conn.close()

        if usuario and check_password_hash(usuario[0], senha):
            session['usuario'] = nm_usuario
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuário ou senha incorretos.', 'danger')

    return render_template('login.html')

@app.route('/criar_usuario')
@login_required
def criar_usuario():
    nm_usuario = 'admin'
    senha_hash = generate_password_hash('admin')

    conn = sqlite3.connect('gestao_hospitalar.db', check_same_thread=False)
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO USUARIO (NM_USUARIO, DS_USUARIO, DS_SENHA) VALUES (?, ?, ?)", 
                       (nm_usuario, 'Administrador', senha_hash))
        conn.commit()
        mensagem = "Usuário criado com sucesso!"
    except sqlite3.IntegrityError:
        mensagem = "Usuário já existe."

    conn.close()
    return mensagem

@app.route('/logout')
@login_required
def logout():
    session.pop('usuario', None)
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
