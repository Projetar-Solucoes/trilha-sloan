import json


ARQUIVO = "solicitacoes.json"


def carregar_dados():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        print("Arquivo ainda não existe. Criando uma lista vazia.")
        return []

    except json.JSONDecodeError:
        print("Erro: o arquivo JSON está inválido.")
        return []


def salvar_dados(solicitacoes):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(
                solicitacoes,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

        print("Dados salvos com sucesso!")

    except Exception as erro:
        print("Erro ao salvar os dados:", erro)


def cadastrar_solicitacao():
    print("\n===== CADASTRAR SOLICITAÇÃO =====")

    try:
        solicitacoes = carregar_dados()

        protocolo = input("Protocolo: ")
        nome = input("Nome: ")
        setor = input("Setor: ")
        categoria = input("Categoria: ")
        assunto = input("Assunto: ")
        descricao = input("Descrição: ")
        prioridade = input("Prioridade: ")

        if nome == "":
            print("O nome não pode ficar vazio.")
            return

        if setor == "":
            print("O setor não pode ficar vazio.")
            return

        if categoria == "":
            print("A categoria não pode ficar vazia.")
            return

        if assunto == "":
            print("O assunto não pode ficar vazio.")
            return

        if descricao == "":
            print("A descrição não pode ficar vazia.")
            return

        if prioridade == "":
            print("A prioridade não pode ficar vazia.")
            return

        nova_solicitacao = {
            "protocolo": protocolo,
            "nome": nome,
            "setor": setor,
            "categoria": categoria,
            "assunto": assunto,
            "descricao": descricao,
            "prioridade": prioridade
        }

        solicitacoes.append(nova_solicitacao)

        salvar_dados(solicitacoes)

        print("Solicitação cadastrada com sucesso!")

    except Exception as erro:
        print("Erro ao cadastrar solicitação:", erro)


def listar_solicitacoes():
    print("\n===== LISTAR SOLICITAÇÕES =====")

    try:
        solicitacoes = carregar_dados()

        if len(solicitacoes) == 0:
            print("Nenhuma solicitação cadastrada.")
            return

        for solicitacao in solicitacoes:
            print("\n-----------------------------")
            print("Protocolo:", solicitacao["protocolo"])
            print("Nome:", solicitacao["nome"])
            print("Setor:", solicitacao["setor"])
            print("Categoria:", solicitacao["categoria"])
            print("Assunto:", solicitacao["assunto"])
            print("Descrição:", solicitacao["descricao"])
            print("Prioridade:", solicitacao["prioridade"])

    except Exception as erro:
        print("Erro ao listar solicitações:", erro)


def consultar_solicitacao():
    print("\n===== CONSULTAR SOLICITAÇÃO =====")

    try:
        solicitacoes = carregar_dados()

        protocolo = input("Digite o protocolo: ")

        for solicitacao in solicitacoes:

            if solicitacao["protocolo"] == protocolo:

                print("\nSolicitação encontrada!")
                print("Protocolo:", solicitacao["protocolo"])
                print("Nome:", solicitacao["nome"])
                print("Setor:", solicitacao["setor"])
                print("Categoria:", solicitacao["categoria"])
                print("Assunto:", solicitacao["assunto"])
                print("Descrição:", solicitacao["descricao"])
                print("Prioridade:", solicitacao["prioridade"])

                return

        print("Protocolo não encontrado.")

    except Exception as erro:
        print("Erro ao consultar solicitação:", erro)


def mostrar_estatisticas():
    print("\n===== ESTATÍSTICAS =====")

    try:
        solicitacoes = carregar_dados()

        total = len(solicitacoes)

        print("Total de solicitações:", total)

        altas = 0
        medias = 0
        baixas = 0

        categorias = {}

        for solicitacao in solicitacoes:

            prioridade = solicitacao["prioridade"].lower()

            if prioridade == "alta":
                altas += 1

            elif prioridade == "média" or prioridade == "media":
                medias += 1

            elif prioridade == "baixa":
                baixas += 1

            categoria = solicitacao["categoria"]

            if categoria in categorias:
                categorias[categoria] += 1
            else:
                categorias[categoria] = 1

        print("\nPor prioridade:")
        print("Alta:", altas)
        print("Média:", medias)
        print("Baixa:", baixas)

        print("\nPor categoria:")

        for categoria in categorias:
            print(categoria + ":", categorias[categoria])

    except Exception as erro:
        print("Erro ao mostrar estatísticas:", erro)