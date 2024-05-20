import sqlite3

class BancoDados:
    def __init__(self):
        self.conexao = sqlite3.connect('.clientes.db')
        self.cursor = self.conexao.cursor()
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                telefone TEXT NOT NULL
            )
        """)
    
    def inserir_cliente(self, cliente):
        self.cursor.execute(""" 
            INSERT INTO clientes(nome, email,telefone)
            VALUES (?,?,?)
        """, (cliente.nome, cliente.email, cliente.telefone))
        self.conexao.commit()

    def listar_clientes(self):
        self.cursor.execute("""
            SELECT id, nome, email, telefone FROM clientes
        """)
        return self.cursor.fetchall()
    
    def atualizar_cliente(self, cliente, cliente_id):
        self.cursor.execute("""
        UPDATE clientes SET
            nome = ?,
            email = ?,
            telefone = ?
        WHERE id = ?
        """, (cliente.nome, cliente.email, cliente.telefone, cliente_id))
        self.conexao.commit()

    def deletar_cliente(self, cliente_id):
        self.cursor.execute("""
        DELETE FROM clientes WHERE id = ?
        """, (cliente_id))
        self.conexao.commit()