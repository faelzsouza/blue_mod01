## Programa que solicita a quantidade de jogos de um usuario e retorna os numeros sorteados para um jogo ##

import random

v = []
m = []
numJogos = 0
sorteio = 6

# Solicita a quantidade de jogos que o usuario deseja.
print("Número de jogos: ")
numJogos = int(input())
print()

# Logica, baseado no conseito de matriz, para sortear e imprimir o(s) jogo(s) do usuario.
i = 0
while i < numJogos:
    i = i + 1
    v.append(i)
    print("Jogo ", len(v) , ":")
    print()
    l = 0
    while l < sorteio:
        r = 0
        r = random.randint(1, 60)
        if r not in m:
            m.insert(l, r)
            print(" - ", m[l] , end = " ")
            l = l + 1
    print(v)
    print(m)