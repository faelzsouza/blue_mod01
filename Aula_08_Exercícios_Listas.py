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
from time import sleep
palavras = ["prego", "luva", "abacate", "caneca", "sorvete"]
palavraSorteada = palavras[randint(0, len(palavras) - 1)]
tracoPalavraSorteada = []

# Cria uma lista com a quantidade de "_" igual a quantidade de letras da palavra sorteada
for l in palavraSorteada:
    tracoPalavraSorteada.append("_")

errosLista = []
erros = 6
forca = ""
print(f"A palavra tem {len(palavraSorteada)} letras")
while erros > 0:
    # A forca ocorre enquanto houver "_" na variável tracoPalavraSorteada
    while "_" in tracoPalavraSorteada:
        chute = input("Qual é o chute? ")
        sleep(0.7)
        # Para cada letra de chute 
        for lchute in chute:
            # Verifica se letra de chute já está na lista de erros
            if lchute in errosLista:
                print(f"Você já tentou essa letra!")
                print(f"Você já tentou {str(errosLista).upper()}")                
            # Verifica se a letra de chute está na palavra sorteada
            elif lchute in palavraSorteada:
                # Para cada letra de palavra sorteada
                for i, l in enumerate(palavraSorteada):
                    # Verifica se a letra da palavra sorteada é igual a letra do chute 
                    if l == lchute:
                        # Altera o underscore de posição igual ao da letra da palavra sorteada pela letra da palavra sorteada
                        tracoPalavraSorteada[i] = lchute
            else:
                # Se não tiver a letra de chute na palavra sorteada
                print(f"\nNa palavra não tem {lchute.upper()}!")
                errosLista.append(lchute)
                erros -= 1
                print(f"Ainda restam {erros} tentativas!")
                print(f"Você já errou {str(errosLista).upper()}")
                # Alternando a carinha de acordo vai errando
                if erros == 5:
                    forca = "😀"
                elif erros == 4:
                    forca = "🙂"
                elif erros == 3:
                    forca = "😶"
                elif erros == 2:
                    forca = "😐"
                elif erros == 1:
                    forca = "😫"
                print(forca)

        print()

        # Printa a lista em forma de palavra
        for l in tracoPalavraSorteada:
            print(l.upper(), end=" ")
        print("\n")
        # Quando erra as 6 vezes printa mensagem final e dá break
        if erros == 0:
            forca = "💀"
            print(forca)
            print(f"\nNão foi dessa vez! A palavra é {palavraSorteada.upper()}!\n")
            break
    break

# Mensagem final se o usuário acertar todas as letras
if erros > 0:
    print("Parabéns! Você acertou! :D\n")


