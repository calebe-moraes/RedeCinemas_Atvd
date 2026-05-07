from repository.cinema_repository import CinemaRepository

class CinemaService:

    def __init__(self):
        self.repository = CinemaRepository()

    def cadastrar_cinema(self, cinema):

        if cinema.capacidade <= 0:
            print("Capacidade inválida!")
            return

        self.repository.cadastrar(cinema)

        print("Cinema cadastrado com sucesso!")

    def listar_cinemas(self):

        cinemas = self.repository.listar_cinemas()

        if not cinemas:
            print("Nenhum cinema cadastrado.")
            return

        for cinema in cinemas:
            print(f"""
ID: {cinema[0]}
Nome: {cinema[1]}
Cidade: {cinema[2]}
Estado: {cinema[3]}
Capacidade: {cinema[4]}
""")