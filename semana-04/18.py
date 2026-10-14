while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 / numero2
    except (ValueError, TypeError):
        print("Erro: digite apenas números.")
        continue
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")
        continue
    else:
        print(f"O valor da divisão de {numero1} por {numero2} é {resultado}")
        break
