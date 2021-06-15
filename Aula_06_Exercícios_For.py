"""01 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte 
quantas vezes aparece as vogais a,e,i,o,u"""
# import unidecode

# string = input("Digite uma frase:\n")
# stringSemAcento = unidecode.unidecode(string)
# vogalA = 0
# vogalE = 0
# vogalI = 0
# vogalO = 0
# vogalU = 0

# for l in stringSemAcento:
#     if l.lower() == "a":
#         vogalA += 1
#     elif l.lower() == "e":
#         vogalE += 1
#     elif l.lower() == "i":
#         vogalI += 1
#     elif l.lower() == "o":
#         vogalO += 1
#     elif l.lower() == "u":
#         vogalU += 1

# print(f"Sua frase tem:")
# print(f"{vogalA} vogal(is) A")
# print(f"{vogalE} vogal(is) E")
# print(f"{vogalI} vogal(is) i")
# print(f"{vogalO} vogal(is) O")
# print(f"{vogalU} vogal(is) U")

"""02 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores"""

# n = int(input("Digite um número: "))
# print(f"O(s) divisor(es) de {n} é/são:")
# for num in range(1, n + 1):
#     if n % num == 0:
#         print(num)


"""03 - Faça um script que o usuário escolha um número de início, um número de fim, e um número de
passo. O programa deve printar todos os números do intervalo entre início e fim, "pulando" de 
acordo com o intervalo passado."""

# inicio = int(input("Início: "))
# fim = int(input("Fim: "))
# intervalo = int(input("Intervalo: "))

# if inicio > fim:
#     for n in range(inicio, fim - 1, -intervalo):
#         print(n, end=" ")
# else:
#     for n in range(inicio, fim + 1, intervalo):
#         print(n, end=" ")

"""04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a 
soma deles (o usuário vai dizer quantos números serão informados antes de começar)"""

# quantosNum = int(input("Quantos números você quer somar? "))
# soma = 0
# for i in range(quantosNum):
#     n = float(input(f"Digite o {i + 1}º número: "))
#     soma += n

# print(f"A soma dos números digitados é: {soma}!")

"""05 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de 
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

# from time import sleep

# print("-" * 44)
# print(" " * 4,"Contagem Regressiva de 10 segundos:")
# print("-" * 44)
# print(" " * 6, end="")
# for i in range(10, 0, -1):
#     print(i, end="")
#     sleep(0.5)
#     print(".", end="")
#     sleep(0.5)
#     print(".", end="")
# print()
# print("-" * 44)
# print("🎆🎆 Que comecem os fogos de artifício! 🎆🎆")
# print("-" * 44)

"""06 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal."""

# from unidecode import unidecode

# frase = input("Digite uma frase: ")

# fraseSemAcento = unidecode(frase)

# fraseSemVogal = ""

# for l in fraseSemAcento:
#     if l.lower() in ["a", "e", "i", "o", "u"]:
#         pass
#     else:
#         fraseSemVogal += l
# print()
# print("Sua frase sem vogal ficou:")
# print(fraseSemVogal)