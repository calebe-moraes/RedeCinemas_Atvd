from model.cinema import Cinema
from service.cinema_service import CinemaService

class CinemaController:

    def __init__(self):
        self.service = CinemaService()

    def cadastrar(self):

        nome = input("Nome do cinema: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        capacidade = int(input("Capacidade: "))

        cinema = Cinema(
            nome,
            cidade,
            estado,
            capacidade
        )

        self.service.cadastrar_cinema(cinema)

    def listar(self):
        self.service.listar_cinemas()