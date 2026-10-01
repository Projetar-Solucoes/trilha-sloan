# Atividade 26.08.2026 - Ravette - Estágio: ProjetAR - EEEP José Ciro Nogueira Machado - Redes de Computadores - 3° Ano - 202/6//
#luthier recebeu um instrumento para manutenção. 
# Operadores e cálculos
# Nome, setor, categoria, assunto e descrição

print("SISTEMA DE LUTHIERIA RAVETTE")

solicitar = input("Você deseja solicitar uma manutenção? (sim/não): ")

if solicitar.lower() == "sim":
    nome = input("\nNome do cliente: ")
    categoria = input("Categoria/Naipe do instrumento: ")
    instrumento = input("Nome do instrumento: ")
    assunto = input("Assunto da manutenção: ")
    descricao = input("Descrição detalhada do problema: ")

    print("\nSolicitação enviada para o luthier!")
    print("Aguarde a análise...")

    print("\nANÁLISE DO LUTHIER")   
    print(f"\nCliente: {nome}")
    print(f"Instrumento: {instrumento}")
    print(f"Categoria/Naipe: {categoria}")
    print(f"Assunto: {assunto}")
    print(f"Descrição: {descricao}")

    print("DECISÃO DO LUTHIER")
    peca = input("Qual peça será utilizada? ")
    valor_peca = float(input(f"Qual(is) o(s) valor da(s) peça(s)? R$ "))
    desconto = float(input("Qual desconto será dado ao cliente? (%) "))
    aceita = input("O luthier aceita realizar a manutenção? (sim/não): ")
    
    if valor_peca < 0 or desconto < 0:
        print("\nErro: o valor da peça e o desconto não podem ser negativos.")

    else:

        subtotal = valor_peca
        valor_desconto = subtotal * desconto / 100
        total = subtotal - valor_desconto

        print("RESULTADO FINAL")
        print(f"\nCliente: {nome}")
        print(f"Instrumento: {instrumento}")
        print(f"Manutenção: {assunto}")
        print(f"descrição: {descricao}")
        print("\nDECISÃO DO LUTHIER")
        print(f"Peça escolhida pelo luthier: {peca}")
        print(f"Valor da peça: R$ {valor_peca:.2f}")

        print(f"\nDesconto definido pelo luthier: {desconto:.1f}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Valor final: R$ {total:.2f}")

        if aceita.lower() == "sim":
            print("\nO LUTHIER ACEITOU A MANUTENÇÃO!")
            print("A peça e o desconto foram definidos pelo luthier.")
            print(f"Valor final do serviço: R$ {total:.2f}")

        else:
            print("\nO LUTHIER RECUSOU A MANUTENÇÃO.")
            print("A solicitação não poderá ser realizada.")

else:
    print("\nSolicitação de manutenção cancelada. Obrigado por utilizar o sistema de luthieria Ravette!")