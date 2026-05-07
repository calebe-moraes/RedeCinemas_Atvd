from model.sessao import Sessao
from service.sessao_service import SessaoService

class SessaoController:

    def __init__(self):
        self.service = SessaoService()

    def cadastrar(self):

        horario = input("Horário da sessão: ")
        publico = int(input("Público: "))
        filme_id = int(input("ID do filme: "))
        cinema_id = int(input("ID do cinema: "))

        sessao = Sessao(
            horario,
            publico,
            filme_id,
            cinema_id
        )

        self.service.cadastrar_sessao(sessao)

    def listar(self):
        self.service.listar_sessoes()