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
    def listar_filmes(self):

        filmes = self.repository.listar_filmes()

        if not filmes:
            print("Nenhum filme cadastrado.")
            return

        for filme in filmes:
            print(f"""
ID: {filme[0]}
Título: {filme[1]}
Duração: {filme[2]} min
Gênero: {filme[3]}
Classificação: {filme[4]}
""")