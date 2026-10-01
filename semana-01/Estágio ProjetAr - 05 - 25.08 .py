# Atividade 27.08.2026 - Ravette - Estágio: ProjetAR - EEEP José Ciro Nogueira Machado - Redes de Computadores - 3° Ano 
# Criar um protocolo no formato ANO-NÚMERO-INICIAIS e testar textos com acentos, maiúsculas e espaços extras.

print("Bem-vindo(a) ao sistema de reclamações da empresa Ravette!")
nome = input("Qual é seu nome? ")
print(f"Olá, {nome}! Seja bem-vindo(a).")
ano = input("Digite o ano da reclamação: ")
resposta = "sim"
nome = nome.upper().split()
iniciais = ''.join([palavra[0] for palavra in nome])
iniciais = ''.join([palavra[0] for palavra in nome])

while resposta.lower() == "sim":
    num_protocolo = input("Digite o número de protocolo: ")
    num_protocolo = num_protocolo.zfill(4)
    protocolo = '-'.join([ano, num_protocolo, iniciais])
    print(f"Protocolo gerado: {protocolo}")
    resposta = input("Deseja fazer outra reclamação? (sim/não): ")

print("Obrigado por utilizar o sistema de reclamações da empresa Ravette! Até a próxima.")
print("Programa Finalizado!")

print("RESUMO: Curso em Vídeo")
# RESUMO: Curso em Vídeo

frase = "Curso em Vídeo Python"

# 1. MOSTRAR A FRASE
print(frase)
# O Python diferencia maiúsculas de minúsculas


# 2. POSIÇÕES E FATIAMENTO
print(frase[9])
# Pega a letra na posição 9, começando do 0
print(frase[9:14])
# Pega as posições 9 até 13 - "Vídeo"
print(frase[9:21:2])
# Pega da posição 9 até 20, pulando de 2 em 2
print(frase[:5])
# Pega da posição 0 até 4 - "Curso"
print(frase[15:])
# Pega da posição 15 até o final - "Python"
print(frase[9::3])
# Pega da posição 9 até o final, pulando de 3 em 3


# 3. TAMANHO DA FRASE
print(len(frase))
# Conta quantos caracteres existem, incluindo espaços


# 4. CONTAR E PROCURAR
print(frase.count('o'))
# Conta quantos "o" existem na frase
print(frase.count('o', 0, 13))
# Conta quantos "o" existem das posições 0 até 12
print(frase.find('deo'))
# Mostra a posição onde "deo" começa
print(frase.find('android'))
# Retorna -1 porque "android" não existe na frase
print('Curso' in frase)
# Retorna True ou False dependendo se "Curso" existe na frase


# 5. SUBSTITUIR
print(frase.replace('Python', 'Android'))
# Substitui "Python" por "Android"
frase = frase.replace('Python', 'Android')
# Substitui "Python" por "Android" e salva a alteração na variável


# 6. MAIÚSCULAS E MINÚSCULAS
print(frase.upper())
# Tudo vira maiúsculo
print(frase.lower())
# Tudo vira minúsculo
print(frase.capitalize())
# Deixa a primeira letra da frase maiúscula
print(frase.title())
# Deixa a primeira letra de cada palavra maiúscula


# 7. ESPAÇOS
print(frase.strip())
# Remove espaços do começo e do final
print(frase.rstrip())
# Remove espaços do final
print(frase.lstrip())
# Remove espaços do começo


# 8. DIVIDIR E JUNTAR
dividido = frase.split()
print(dividido)
# Separa as palavras e transforma em uma lista
print(' '.join(dividido))
# Junta as palavras usando espaço entre elas


# 9. ACESSAR UMA PALAVRA DA LISTA
print(dividido[0])
# Pega a primeira palavra da lista
print(dividido[0][3])
# Pega a primeira palavra da lista e depois a letra na posição 3


# 10. COMBINANDO FUNÇÕES
print(frase.upper().count('O'))
# Deixa tudo maiúsculo e conta quantos "O" existem
print(frase.lower().find('python'))
# Deixa tudo minúsculo e procura "python"
