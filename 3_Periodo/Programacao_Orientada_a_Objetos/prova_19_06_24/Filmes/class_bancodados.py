import sqlite3
class BancoDados:
    def __init__(self):
        self.conexao = sqlite3.connect('filmes.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                ano TEXT,genero TEXT, runtime TEXT, diretor TEXT
            )
        """)
    def inserir_filme(self, filme):
        self.cursor.execute("""
            INSERT INTO filmes (titulo, ano, genero, runtime, diretor)
            VALUES (?, ?, ?, ?, ?)
        """, (filme.titulo, filme.ano, filme.genero, filme.runtime, filme.diretor))
        self.conexao.commit()

    def listar_filmes(self):
        self.cursor.execute("""
            SELECT id, titulo, ano, genero, runtime, diretor FROM filmes
        """)
        return self.cursor.fetchall()

    def atualizar_filme(self, filme, filme_id):
        self.cursor.execute("""
            UPDATE filmes SET
                titulo = ?,
                ano = ?,
                genero = ?,
                runtime = ?,
                diretor = ?
            WHERE id = ?
        """, (filme.titulo, filme.ano, filme.genero, filme.runtime, filme.diretor, filme_id))
        self.conexao.commit()

    def deletar_filme(self, filme_id):
        self.cursor.execute("""
            DELETE FROM filmes WHERE id = ?
        """, (filme_id,))
        self.conexao.commit()