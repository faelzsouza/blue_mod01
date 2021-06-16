"""
Execute as atividades abaixo, utilizando a estrutura de repetição FOR:
#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
o maior e o menor peso lidos.
"""
# numeroPessoas = 5
# maior = 0
# menor = float('inf')
# for i in range(numeroPessoas):
#     peso = float(input("Qual é o seu peso? "))
#     if peso > maior:
#         maior = peso
#     elif peso < menor:
#         menor = peso

# print()
# print(f'O maior peso é {maior}\nO menor peso é {menor}')

"""
#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
tabuada desse número.
"""

# n = int(input("Digite um número inteiro: "))
# print(f'Tabuada de {n}:')
# for num in range(1, 11):
#     print(f'{n} x {num} = {n * num}')

"""
#03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
maiores.
"""

# quantidadePessoas = 7
# maiorIdade = 0
# menorIdade = 0
# ano = 2021
# for p in range(1, quantidadePessoas + 1):
#     anoNasc = int(input(f'Qual é o {p}º ano de nascimento?'))
#     idade = ano - anoNasc
#     if idade >= 18:
#         maiorIdade += 1
#     else:
#         menorIdade += 1
# print()
# print(f'{maiorIdade} maior(es) de idade.\n{menorIdade} menor(es) de idade.')

"""
#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
Mostre também quantos valores pares foram digitados.
"""

# somaPares = 0
# quantosNum = 6

# for n in range(1, quantosNum + 1):
#     num = int(input(f'Digite o {n}º número: '))
#     if num % 2 == 0:
#         somaPares += num

# print()
# print(f'A soma dos pares é {somaPares}.')

"""
Execute as atividades abaixo, utilizando a estrutura de repetição WHILE:
#01 - Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
sem break)
"""

flag1 = True
flag2 = True
tracos = '=-=' * 8
while flag1:
    flag1 = True
    flag2 = True
    print(tracos)
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    soma = n1 + n2
    mult = n1 * n2
    maior = 0
    while flag2:
        print("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
        """)
        acao = int(input('Qual ação acima deseja executar?\n'))
        if acao == 1:
            print(f'\n{n1} + {n2} = {soma}')
            print(tracos)
        elif acao == 2:
            print(f'\n{n1} x {n2} = {mult}')
            print(tracos)
        elif acao == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print(f'\nO maior número é o {maior}')
            print(tracos)
        elif acao == 4:
            flag2 = False
        elif acao == 5:
            print(tracos)
            print(" Programa Encerrado :D")
            print(tracos)
            flag2 = False
            flag1 = False


        


"""
#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
#03 - Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
(C) Qual é o nome do produto mais barato.#04 (DESAFIO) Crie um jogo onde o computador vai “pensar” em um número entre
0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os
palpites diga ao jogador se o número do computador é maior ou menor ao que ele
digitou,no final mostre quantos palpites foram necessários para vencer.
#05 (DESAFIO) Em uma eleição presidencial existem quatro candidatos. Os votos
são informados por meio de código.
Os códigos utilizados são:
1 , 2, 3 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - José / 2- João / etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos

"""