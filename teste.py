# Construir um código em qualquer linguagem que some os números ímpares de 1 (inclusive) a 10 (inclusive), deve conter loop e decisão.

soma = 0
for n in range(1, 11):
    if n % 2 == 1:
        soma += n

print(soma)
