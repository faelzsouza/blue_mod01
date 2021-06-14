# -*- coding: utf-8 -*-
"""Exercicios_aula05_while.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ATPk51bcklERbn9_Z5dSbFGkpAvLlnk3

1 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

while True:
  sexo = input("Qual é o seu sexo? [F/M]\n").lower().strip()[0]
  if sexo == "f" or sexo == "m":
    break
  else:
    print("Digite novamente!")

"""2 - Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem
corretamente a senha. A senha é “Blue123”
"""

while True:
  senha = input("Digite a senha: ")
  if senha == "Blue123":
    print("Senha correta!")
    break
  print("Senha incorreta! Tente novamente...")

"""2b - Exiba quantas vezes o usuário errou a digitação."""

tentativas = 0
while True:
  senha = input("Digite a senha: ")
  if senha == "Blue123":
    print("Senha correta!")
    break
  tentativas += 1
  print(f"Senha incorreta! Você já errou {tentativas} vez(es)")

"""3 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa 
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No 
final, mostre:<br>
A) Quantas pessoas tem mais de 18 anos.<br>
B) Quantos homens foram cadastrados.<br>
C) Quantas mulheres tem menos de 20 anos.<br>

"""

maiores18 = 0
homem = 0
mulherMenor20 = 0
while True:
  idade = int(input("Qual é a idade?\n"))
  sexo = input("Qual é o sexo? [F/M]\n").lower().strip()[0]
  if idade > 18: maiores18 += 1
  if sexo == "m": homem += 1
  if idade < 20 and sexo == "f": mulherMenor20 += 1
  while True:
    resp = input("Deseja continuar cadastrando? [S/N] ").lower().strip()[0]
    if resp == "n":
      print()
      if maiores18 > 1: 
        print(f"Foram cadastradas {maiores18} pessoas maiores de 18 anos.")
      else:
        print(f"Foi cadastrada {maiores18} pessoa maior de 18 anos.")
      if homem > 1:
        print(f"Foram cadastrados {homem} homens.")
      else:
        print(f"Foi cadastrado {homem} homem.")
      if mulherMenor20 > 1:
        print(f"Foram cadastradas {mulherMenor20} mulheres que tem menos de 20 anos.")
      else:
        print(f"Foi cadastrada {mulherMenor20} mulher que tem menos de 20 anos.")
      break
    else:
      print("Opção Inválida!!")
  break

"""DESAFIO:<br>
4 - Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar 
adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram 
necessários para vencer.
"""

from random import randint
erro = 0
numeroAleatorio = randint(0, 10)
while True:
  palpite = int(input("Você só vencerá esse desafio se descobrir\nqual número estou pensando de 0 a 10:\n "))
  if palpite == numeroAleatorio:
    print()
    print("Parabéns, você ACERTOU!")
    print(f"Você errou {erro} vez(es).")
    break
  else:
    print()
    erro += 1
    if palpite < numeroAleatorio:
      print(f"Errou!! O número é maior do que {palpite}.")
      print()
    else:
      print(f"Errou!! O número é menor do que {palpite}.")
      print()

"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.

"""

n = int(input("Do 1 até qual número você deseja ver os números primos? "))
c = 2
divisoes = 0
quebralinha = 0
vinte1 = 21
primos = ""
while c <= n:
  flag = False
  for cont in range(2, c):
    if c % cont == 0:
      flag = True
      divisoes += 1
      break
  if flag == False:
    primos += f"{c} "
    quebralinha += 1
    if quebralinha == vinte1:
      primos += "\n"
      vinte1 += 21 - 5
  c += 1

print(f"O(s) número(s) primo(s) de 1 a {n} é(são):")
print(f"{primos.strip()}\n\nDivisões realizadas: {divisoes}")

 