"""
#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.
"""

# lista = []
# flag = True
# cont = 1
# while flag:
#     numero = int(input(f'Digite o {cont}º número: '))
#     if numero in lista:
#         print(f'Número {numero} já está na lista!')
#     else:
#         lista.append(numero)
#     while True:
#         continuar = input("Deseja continuar? [S/N] ").lower()[0]
#         if continuar == 'n':
#             flag = False
#             break
#         elif continuar == 's':
#             break
#         else:
#             print('Opção Inválida!!')
#     cont += 1
# lista.sort()
# print(lista) 

"""
#02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
geradas.
"""

# lista = []
# listaPar = []
# listaImpar = []
# cont = 1
# flag = True
# while flag:
#     numero = int(input(f'Digite o {cont}º número: '))
#     lista.append(numero)
#     if numero % 2 == 0:
#         listaPar.append(numero)
#     else:
#         listaImpar.append(numero)
#     while True:
#         continuar = input("Deseja continuar? [S/N]").lower()[0]
#         if continuar == "s":
#             break
#         elif continuar == "n":
#             flag = False
#             break
#         else:
#             print("Opção Inválida!!!")
#     cont += 1


# print("Lista Completa:", lista)
# print("Lista de Números Ímpares:", listaImpar)
# print("Lista de Números Pares:", listaPar)

"""
Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

# from random import randint

# listaPrincipal = []
# quantidadeJogos = int(input("Quantos jogos deseja gerar? "))
# print()
# for q in range(quantidadeJogos):
#     listaPalpite = []
#     for n in range(6):
#         while True:
#             numero = randint(1, 60)
#             if numero in listaPalpite:
#                 pass
#             else:
#                 listaPalpite.append(numero)
#                 break
#     listaPrincipal.append(listaPalpite)

# cont = 0
# for jogo in listaPrincipal:
#     cont += 1
#     print(f'Jogo {cont}: {jogo}')

# print("\nBoa sorte!!!")
