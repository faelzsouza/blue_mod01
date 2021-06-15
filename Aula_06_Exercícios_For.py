# 01 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte 
# quantas vezes aparece as vogais a,e,i,o,u
import unidecode

string = input("Digite uma frase:\n")
stringSemAcento = unidecode.unidecode(string)
vogalA = 0
vogalE = 0
vogalI = 0
vogalO = 0
vogalU = 0

for l in stringSemAcento:
    if l.lower() == "a":
        vogalA += 1
    elif l.lower() == "e":
        vogalE += 1
    elif l.lower() == "i":
        vogalI += 1
    elif l.lower() == "o":
        vogalO += 1
    elif l.lower() == "u":
        vogalU += 1

print(f"Sua frase tem:")
print(f"{vogalA} vogal(is) A")
print(f"{vogalE} vogal(is) E")
print(f"{vogalI} vogal(is) i")
print(f"{vogalO} vogal(is) O")
print(f"{vogalU} vogal(is) U")

# 02 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores



# 03 - Faça um script que o usuário escolha um número de início, um número de fim, e um número de
# passo. O programa deve printar todos os números do intervalo entre início e fim, "pulando" de 
# acordo com o intervalo passado.



# 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a 
# soma deles (o usuário vai dizer quantos números serão informados antes de começar)



# 05 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de 
# artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.



# 06 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

