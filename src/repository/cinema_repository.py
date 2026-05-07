import sqlite3

class CinemaRepository:

    def cadastrar(self, cinema):

        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO cinemas (
            nome,
            cidade,
            estado,
            capacidade
        )
        VALUES (?, ?, ?, ?)
        """, (
            cinema.nome,
            cinema.cidade,
            cinema.estado,
            cinema.capacidade
        ))

        conexao.commit()
        conexao.close()

    def listar_cinemas(self):

        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM cinemas")

        cinemas = cursor.fetchall()

        conexao.close()

        return cinemas