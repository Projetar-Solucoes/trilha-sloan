import funcoes


def main():
    while True:
        print("\n===== CENTRAL DE SOLICITAÇÕES =====")
        print("1 - Cadastrar solicitação")
        print("2 - Listar solicitações")
        print("3 - Consultar solicitação")
        print("4 - Mostrar estatísticas")
        print("5 - Sair")

        try:
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                funcoes.cadastrar_solicitacao()

            elif opcao == "2":
                funcoes.listar_solicitacoes()

            elif opcao == "3":
                funcoes.consultar_solicitacao()

            elif opcao == "4":
                funcoes.mostrar_estatisticas()

            elif opcao == "5":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida!")

        except Exception as erro:
            print("Ocorreu um erro:", erro)


main()