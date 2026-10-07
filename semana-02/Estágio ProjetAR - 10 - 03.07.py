def verificar_emprestimo(parcela, renda):
    limite = renda * 0.3
    return parcela <= limite


# Entrada dos dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cpf = int(input("Digite seu CPF: "))
renda = float(input("Digite sua renda: "))


# Validação dos dados
if nome.strip() == "":
    print("Nome inválido.")

elif idade < 18:
    print("Você precisa ser maior de idade.")

elif len(str(cpf)) != 11:
    print("CPF inválido.")

else:
    # Dados do empréstimo
    emprestimo = float(input("Digite o valor do empréstimo: "))
    ano = int(input("Digite em quantos anos deseja pagar: "))

    parcela = emprestimo / (ano * 12)

    # Análise do empréstimo
    if renda < 1500 or renda > 50000:
        print("Empréstimo não aprovado.")
        print("A renda está fora dos limites permitidos.")

    elif not verificar_emprestimo(parcela, renda):
        print("Empréstimo não aprovado.")
        print("O valor da parcela é muito alto para sua renda.")

    elif renda == 1500 or 20001 <= renda <= 50000:
        print("Empréstimo encaminhado para revisão humana.")

    else:
        print("Empréstimo aprovado!")
        print("Liberação automática autorizada.")