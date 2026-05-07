from repository.sessao_repository import SessaoRepository

class SessaoService:

    def __init__(self):
        self.repository = SessaoRepository()

    def cadastrar_sessao(self, sessao):

        if sessao.publico < 0:
            print("Público inválido!")
            return

        self.repository.cadastrar(sessao)

        print("Sessão cadastrada com sucesso!")

    def listar_sessoes(self):

        sessoes = self.repository.listar_sessoes()

        if not sessoes:
            print("Nenhuma sessão cadastrada.")
            return

        for sessao in sessoes:
            print(f"""
ID: {sessao[0]}
Horário: {sessao[1]}
Público: {sessao[2]}
Filme: {sessao[3]}
Cinema: {sessao[4]}
""")