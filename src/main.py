from controller.filme_controller import FilmeController
from controller.cinema_controller import CinemaController
from controller.sessao_controller import SessaoController

filme_controller = FilmeController()
cinema_controller = CinemaController()
sessao_controller = SessaoController()

while True:

    print("\n===== REDE DE CINEMAS =====")
    print("1 - Cadastrar Filme")
    print("2 - Listar Filmes")
    print("3 - Cadastrar Cinema")
    print("4 - Listar Cinemas")
    print("5 - Cadastrar Sessão")
    print("6 - Listar Sessões")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        filme_controller.cadastrar()

    elif opcao == "2":
        filme_controller.listar()

    elif opcao == "3":
        cinema_controller.cadastrar()

    elif opcao == "4":
        cinema_controller.listar()

    elif opcao == "5":
        sessao_controller.cadastrar()

    elif opcao == "6":
        sessao_controller.listar()

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")