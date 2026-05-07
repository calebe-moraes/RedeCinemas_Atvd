from repository.filme_repository import FilmeRepository

class FilmeService:

    def __init__(self):
        self.repository = FilmeRepository()

    def cadastrar_filme(self, filme):

        if filme.duracao <= 0:
            print("Duração inválida!")
            return

        self.repository.cadastrar(filme)

        print("Filme cadastrado com sucesso!")