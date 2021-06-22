"""
1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, 
verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela 
a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' 
e também quantos são maiores e quantos são menores de idade.
"""
# clientes = []
# maiorIdade = []
# menorIdade = []
# for i in range(1, 6):
#     cliente = []
#     nome = input(f"Qual é o nome do {i}º cliente: ")
#     idade = int(input("Qual é a idade dele(a)? "))
#     if idade >= 18:
#         maiorIdade.append(nome)
#     else:
#         menorIdade.append(nome)
#     cliente.append(nome)
#     cliente.append(idade)
#     clientes.append(cliente)
# qMaiorIdade = len(maiorIdade)
# qMenorIdade = len(menorIdade)
# for c in clientes:
#     if c[1] >= 18:
#         print(f"{c[0]} é maior de idade!")
#     else:
#         print(f"{c[0]} é menor de idade!")
# print(f"{qMaiorIdade} é/são maior(es) de idade.")
# print(f"{qMenorIdade} é/são menor(es) de idade.")

"""
2 - Faça um programa que leia nome e altura de várias pessoas, guardando tudo em uma lista, 
depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o 
programa. No final mostre:
# Quantas pessoas foram cadastradas
# Mostre a maior altura
# Mostre a menor altura
"""
# listaPessoas = []
# flag = True
# cont = 0
# while flag:
#     pessoa = []
#     nome = input("Nome: ")
#     pessoa.append(nome.title())
#     altura = float(input("Altura: "))
#     pessoa.append(altura)
#     listaPessoas.append(pessoa)
#     cont += 1
#     while True:
#         continuar = input("Adicionar mais pessoas? [S/N] ")
#         if continuar.lower()[0] == "n":
#             flag = False
#             break
#         elif continuar.lower()[0] == "s":
#             break
#         else:
#             print("Opção inválida!")
# maiorAltura = 0
# menorAltura = 10
# for p in listaPessoas:
#     if p[1] > maiorAltura:
#         maiorAltura = p[1]
#     elif p[1] < menorAltura:
#         menorAltura = p[1]
# print(cont, "cadastrado(s)")
# print("Maior altura:", maiorAltura)
# print("Menor altura:", menorAltura)