from controller.filme_controller import FilmeController

controller = FilmeController()

while True:

    print("\n===== REDE DE CINEMAS =====")
    print("1 - Cadastrar Filme")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        controller.cadastrar()

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")