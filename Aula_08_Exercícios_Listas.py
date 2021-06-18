"""
1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
a) tamanho da lista.
b) maior valor da lista.
c) menor valor da lista.
d) soma de todos os elementos da lista.
e) lista em ordem crescente.
f) lista em ordem decrescente.
"""



"""
2- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As 
perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a 
pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 
como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""

# print("=-=" * 10)
# print(" " * 4,"PROJETO 01 - DETETIVE")
# print("=-=" * 10)
# cont = 0
# traco = "-" * 30
# perguntas = ["Você telefonou para a vítima?\n[S/N] ", "Você esteve no local do crime?\n[S/N] ", "Você mora perto da vítima?\n[S/N] ", "Você devia para a vítima?\n[S/N] ", "Você já trabalhou com a vítima?\n[S/N] "]

# for p in perguntas:
#     while True:
#         resposta = input(p)
#         if resposta.lower().strip()[0] == "s":
#             cont = cont + 1
#             break
#         elif resposta.lower().strip()[0] == "n":
#             break
#         else:
#             print("Opção inválida! Digite [S] ou [N]!")
#         print(traco)
# resul = "Classificação: "
# if cont == 2:
#   resul = resul + "Suspeito(a)"
# elif 3 <= cont <=4:
#   resul = resul + "Cúmplice"
# elif cont == 5:
#   resul = resul + "Assassino(a)"
# else:
#   resul = resul + "Inocente"
# print(resul)
# print("=-=" * 10)
# print(" " * 7, "CASO ENCERRADO!")
# print("=-=" * 10)

"""
3- Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e 
escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado
"""

from random import randint
palavras = ["prego", "luva", "abacate", "caneca", "sorvete"]
palavraSorteada = palavras[randint(0, len(palavras) - 1)]
word = "AMAR"
tracoPalavraSorteada = []
for l in word:
    tracoPalavraSorteada.append("_")

erros = []

while "_" in tracoPalavraSorteada:
    index = 0
    chute = input("Qual é o chute? ")
    if chute in word:
        for l in word:
            if l == chute:
                tracoPalavraSorteada[index] = chute
            index += 1
    for l in tracoPalavraSorteada:
        print(l, end="")

for l in tracoPalavraSorteada:
    print(l, end="")