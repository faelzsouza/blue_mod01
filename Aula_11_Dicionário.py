# vingadores = {"Chris Evans":"Capitão América", "Mark Ruffalo":"Hulk", "Tom Hiddleston":"Loki", "Chris Hemworth":"Thor", "Robert Downey Jr":"Homem de Ferro", "Scarlett Johansson":"Viúva Negra"}
# for i in vingadores:
#     print(f"{i}: {vingadores[i]}")

"""
2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
"""
# lista = [1, 4, 5, 6, 7, 9]
# dic = {}
# for n in lista:
#     dic[n] = n**2

# print(dic)

"""Exercício 3- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.
"""
from time import sleep

estoque = {"batata": 10, 'feijão': 5, 'arroz': 2, 'café': 0, 'leite': 1}
compra_total = [0, 0]
while True:
    compra = input('Qual item deseja comprar? Para sair digite 0!\n')
    if compra == "0":
            break
    elif estoque.get(compra) == None:
        print('Produto em falta no momento!')
    else:
        qntd = float(input('Qual a quantidade? '))
        if estoque[compra] == 0:
            print(f'O estoque de {compra.upper()} está zerado! :/')
        elif estoque[compra] < qntd:
            print(f'Vixe, só temos {estoque[compra]} desse item!')
        else:
            compra_total[0] += 1
            compra_total[1] += qntd
            print('\nOK!\n')
print('\nProduto(s) sendo ensacolado(s)..!\n')
sleep(1)
print(f"Você comprou um total de {int(compra_total[1])} item(ns) em {compra_total[0]} compra(s)!")
