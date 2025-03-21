from werkzeug.security import generate_password_hash
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('gestao_hospitalar.db')
cursor = conn.cursor()

# Criação da tabela de usuários (caso ainda não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS USUARIO (
        NM_USUARIO TEXT PRIMARY KEY,
        DS_USUARIO TEXT,
        DS_SENHA TEXT NOT NULL,
        TIPO_USUARIO TEXT NOT NULL
    );
''')

# Definindo a senha para o admin inicial
senha_admin = generate_password_hash('admin')  # Senha "admin" para o usuário admin

# Inserir o usuário admin
cursor.execute("INSERT INTO USUARIO (NM_USUARIO, DS_USUARIO, DS_SENHA, TIPO_USUARIO) VALUES (?, ?, ?, ?)", 
               ('admin', 'admin', senha_admin, 'admin'))

# Commit para salvar as alterações
conn.commit()
conn.close()

print("Usuário admin criado com sucesso!")
