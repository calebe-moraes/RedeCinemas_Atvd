from model.filme import Filme
from service.filme_service import FilmeService

class FilmeController:

    def __init__(self):
        self.service = FilmeService()

    def cadastrar(self):

        titulo = input("Título do filme: ")
        duracao = int(input("Duração em minutos: "))
        genero = input("Gênero: ")
        classificacao = input("Classificação: ")

        filme = Filme(
            titulo,
            duracao,
            genero,
            classificacao
        )

        self.service.cadastrar_filme(filme)
    def listar(self):
        self.service.listar_filmes()