# Aula 07 - Testes 
nome = input("Qual é o seu nome? ")

print('Olá, {}! Seja bem-vindo(a) à aula de Python!'.format(nome))
print('Olá, {:20}! Seja bem-vindo(a) à aula de Python!'.format(nome))
print('Olá, {:>20}! Seja bem-vindo(a) à aula de Python!'.format(nome))
print('Olá, {:^20}! Seja bem-vindo(a) à aula de Python!'.format(nome))

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print('A soma de {} e {} é: {}'.format(n1, n2, n1+n2))
print('A subtração de {} e {} é: {}'.format(n1, n2, n1-n2))
print('A multiplicação de {} e {} é: {}'.format(n1, n2, n1*n2))
print('A divisão de {} e {} é: {}'.format(n1, n2, n1/n2))
print('A divisão inteira de {} e {} é: {}'.format(n1, n2, n1//n2))
print('O resto da divisão de {} e {} é: {}'.format(n1, n2, n1%n2))
print('A potência de {} e {} é: {}'.format(n1, n2, n1**n2))
print('O sucessor de {} é {} e o antecessor é {}'.format(n1, n1+1, n1-1, n1-1))

aln1 = int(input("Digite nota do primeiro período: "))
aln2 = int(input("Digite nota do segundo período: "))
aln3 = int(input("Digite nota do terceiro período: "))
aln4 = int(input("Digite nota do quarto período: "))

media = (aln1 + aln2 + aln3 + aln4) / 4
if media >= 7:
    print('Parabéns! Você foi aprovado(a) com média {:.2f}'.format(media))
else:
    print('Infelizmente você foi reprovado(a) com média {:.2f}'.format(media))

    # Atividade 25.08.2026 - Ravette - Estágio: ProjetAR - EEEP José Ciro Nogueira Machado - Redes de Computadores - 3° Ano - 2026


area = input("Digite sua área: ")  
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))  
experiencia = input("Digite sua experiência: ")  
print(f"Olá, {nome}, você tem {idade} anos, mede {altura} metros, atua em {area} e tem experiência em {experiencia}.")
print(type(nome))
print(type(idade))
print(type(altura))
print(type(area))
print(type(experiencia)) 
nome2 = input("Qual é o seu nome? ") 
print(f"Prazer em te conhecer {nome2:=^20}!")  # MUDANÇA: centralizado
print(f"Prazer em te conhecer {nome2:->20}!")  # MUDANÇA: direita
print(f"Prazer em te conhecer {nome2:-<20}!")  # MUDANÇA: esquerda
print(f"Prazer em te conhecer {nome2:-^20}!")  # MUDANÇA: centralizado com traços

num1 = int(input("Digite um número: ")) 
num2 = int(input("Digite outro número: "))  

soma = num1 + num2
potencia = num1 ** num2 
resto = num1 % num2
multiplicacao = num1 * num2
divisao = num1 / num2
subtracao = num1 - num2
inteira = num1 // num2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao:.3f}")
print(f"Divisão inteira: {inteira}")
print(f"Potência: {potencia}")
print(f"Resto: {resto}")