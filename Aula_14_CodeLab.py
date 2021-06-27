"""
Exercícios

1.	Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""
# def soma(n1, n2, n3):
#     total = n1 + n2 + n3
#     print(total)

# n1 = int(input('Digite o 1º número: '))
# n2 = int(input('Digite o 2º número: '))
# n3 = int(input('Digite o 3º número: '))

# soma(n1, n2, n3)
"""
2.	 Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.
"""
# def validaNumero(n):
#     if n > 0:
#         print('P')
#     elif n < 0:
#         print('N')
#     else:
#         print(n)

# num = int(input('Digite um número inteiro: '))
# validaNumero(num)

"""
3.	 Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""
# def somaImposto(taxaImposto, custo):
#     custo += custo * taxaImposto / 100
#     print(f'Valor atualizado: R${custo:.2f}')

# taxaImposto = float(input('Taxa de Imposto: '))
# custo = float(input('Custo: '))

# somaImposto(taxaImposto, custo)
"""
4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.
"""
# salario = 5000
# def calculaSalario(horas):
#     salarioHora = salario / 40
#     salarioRecebido = salarioHora * horas
#     if horas > 40:
#         horasExtras = horas - 40
#         salarioRecebido = salario
#         valorHorasExtras = horasExtras * salarioHora * 1.5
#         salarioRecebido += valorHorasExtras
#     print(f'Seu salário será R${salarioRecebido:.2f}')

# horas = float(input('Quantas horas você trabalhou? '))
# calculaSalario(horas)


"""
5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
"""
# def imc():
#     calculo = 75 / (1.68**2)
#     print(f'IMC: {calculo:.1f}')

# imc()
"""
6.	Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

Nota	Conceito
>=9.0	A
>=8.0	B
>=7.0	C
>=6.0	D
<=4.0	F
"""
# def notaConceito(nota):
#     if nota >= 9:
#         nota = 'A'
#     elif nota >= 8:
#         nota = 'B'
#     elif nota >= 7:
#         nota = 'C'
#     elif nota >= 6:
#         nota = 'D'
#     elif nota <= 5:
#         nota = 'F'
    
#     print(f'Conceito {nota}!')

# nota = float(input('Digite a nota: '))

# notaConceito(nota)
    
"""
7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.
"""
# def menorOuIgual(n1, n2):
#     if n1 < n2:
#         print(f'O menor é {n1}')
#     elif n2 < n1:
#         print(f'O menor é {n2}')
#     else:
#         print('Os números são iguais!')

# n1 = float(input('Digite um número: '))
# n2 = float(input('Digite outro número: '))

# menorOuIgual(n1, n2)

"""
DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.
"""
