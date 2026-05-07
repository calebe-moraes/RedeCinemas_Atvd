import sqlite3

class FilmeRepository:

    def cadastrar(self, filme):

        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO filmes (
            titulo,
            duracao,
            genero,
            classificacao
        )
        VALUES (?, ?, ?, ?)
        """, (
            filme.titulo,
            filme.duracao,
            filme.genero,
            filme.classificacao
        ))

        conexao.commit()
        conexao.close()

    def listar_filmes(self):

        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM filmes")

        filmes = cursor.fetchall()

        conexao.close()

        return filmes