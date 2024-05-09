import sqlite3
from class_cliente import Cliente

def aaaa(self):
    self.cursor.execute("""
    CREATE TALE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        telefone TEXT NOT NULL
    )
    """)

    def inserir_cliente(self,cliente):
        self.cursor.execute("""
            INSERT INTO clientes (nome,email,telefone)
            VALUES (?,?,?)
            """), (cliente.nome, cliente.email, cliente.telefone)
        self.conexao.commit()

    def listar_clientes(self):
        self.cursor.execute("""
            SELECT id, nome, email, telefone, FROM clientes
        """)
        return self.cursor.fetchall()
    
    def atualizar_cliente(self,cliente):
        