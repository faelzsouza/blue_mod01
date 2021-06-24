"""3. Faça um programa que leia nome e média de um aluno, guardando também a situação 
em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para 
aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é 
reprovado.
"""

# alunos = {}
# flag = True
# while flag:
#     nome = input("Nome do Aluno: ")
#     media = float(input("Média do Aluno: "))

#     alunos[nome] = media

#     while True:
#         continuar = input("Deseja adicionar mais aluno? [S/N]").lower()[0]
#         if continuar == 's':
#             break
#         elif continuar == 'n':
#             flag = False
#             break
#         else:
#             print('Opção inválida!')

# for a in alunos:
#     if alunos[a] >= 7:
#         print(f'{a} = APROVADO!')
#     elif 5 <= alunos[a] < 7:
#         print(f'{a} = RECUPERAÇÃO!')
#     elif alunos[a] < 5:
#         print(f'{a} = REPROVADO!')

"""
4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário 
receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve 
contribuir por 35 anos para se aposentar.
"""

# trabalhadores = {}

# flag = True

# while flag:
#     nome = input('Nome: ')
#     anoNasc = int(input('Ano de Nascimento: '))
#     ctps = int(input('Nº CTPS: '))

"""
5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma 
lista. No final, mostre:
A) Quantas pessoas estão cadastradas.
B) A média da idade.
C) Uma lista com as mulheres.
D) Uma lista com as idades que estão acima da média.
OBS: O programa deve garantir que o sexo digitado seja válido, e que quando 
perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
"""



"""
6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que 
calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios 
apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as 
situações dos 15 alunos de uma vez só.
"""

# alunos = {}
# flag = True
# nNotas = 5
# while flag:
#     notas = []
#     nome = input("Nome do Aluno: ")
#     for i in range(1, nNotas + 1):
#         nota = float(input(f"{i}ª nota: "))
#         notas.append(nota)

#     alunos[nome] = {'notas': notas}

#     while True:
#         continuar = input("Deseja adicionar mais aluno? [S/N] ").lower()[0]
#         if continuar == 's':
#             break
#         elif continuar == 'n':
#             flag = False
#             break
#         else:
#             print('Opção inválida!')



# for a in alunos:
#     notatotal = sum(alunos[a]['notas'])
#     media = notatotal / len(alunos[a]['notas'])
#     alunos[a]['media'] = media
#     if media >= 7:
#         alunos[a]['situacao'] = 'APROVADO'
#     elif 5 <= media < 7:
#         alunos[a]['situacao'] = 'RECUPERAÇÃO'
#     elif media < 5:
#         alunos[a]['situacao'] = 'REPROVADO'

# print()

# print('RESULTADO ALUNOS:')
# for a in alunos:
#     print(format(f'{a.upper()}, notas: {alunos[a]["notas"]}, média: {alunos[a]["media"]:.1f}, situação: {alunos[a]["situacao"]}','^'))