import sqlite3

class SessaoRepository:

    def cadastrar(self, sessao):

        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO sessoes (
            horario,
            publico,
            filme_id,
            cinema_id
        )
        VALUES (?, ?, ?, ?)
        """, (
            sessao.horario,
            sessao.publico,
            sessao.filme_id,
            sessao.cinema_id
        ))

        conexao.commit()
        conexao.close()

    def listar_sessoes(self):

        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT
            sessoes.id,
            sessoes.horario,
            sessoes.publico,
            filmes.titulo,
            cinemas.nome
        FROM sessoes
        JOIN filmes
            ON sessoes.filme_id = filmes.id
        JOIN cinemas
            ON sessoes.cinema_id = cinemas.id
        """)

        sessoes = cursor.fetchall()

        conexao.close()

        return sessoes