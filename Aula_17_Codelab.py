# 1) Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado. Não esqueça que os lançamentos são feitos de forma randômica.

# import random

# class Lancador():

#     def __init__(self, escolha):
#         self.escolha = escolha.upper()

#     def lançarDado (self):
#         r = random.randint(1,6)
#         print(f"O dado sorteou o numero {r}.")

#     def lançarMoeda(self):
#         r = random.randint(1,2)
#         if r == 1:
#             r = "Cara"
#         else:
#             r = "Coroa"        
#         print(f"Moeada caiu {r}.")

#     def escolher (self):
#         if self.escolha == "DADO":
#             self.lançarDado()
#         else:
#             self.lançarMoeda()    

# l = input("Escolha oque vc deseja lançar. DADO ou MOEDA: ")

# lancar = Lancador(l)
# lancar.escolher()

# 2) Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.

# class Jogador():
#     def __init__(self, nome, partidas):
#         self.nome = nome.capitalize()
#         self.partidas = partidas
#         self.gols = {'nome': nome, 'partidas': partidas}

#     def contagemGols(self):
#         lista = []
#         for p in range(self.partidas):
#             golsPartida = int(input(f'Quantos gols na {p+1}ª partida: '))
#             lista.append(golsPartida)
#         self.gols['golsPartida'] = lista
#         self.somaGols()

#     def somaGols(self):
#         self.gols['totalGols'] = sum(self.gols['golsPartida'])

#     def mostraDic(self):
#         return self.gols

# nome = input('Nome do jogador: ')
# partidas = int(input('Quantas partidas: '))

# j1 = Jogador(nome, partidas)
# j1.contagemGols()
# print(j1.mostraDic())

# 3) Vamos aprimorar o código:  cadastro de jogador de futebol.py que foi desenvolvido no Code Lab da aula 14. Faça com que o seu código funcione para vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador. 

# class Jogador():
#     def __init__(self, nome, partidas):
#         self.nome = nome.capitalize()
#         self.partidas = partidas
#         self.gols = {'nome': nome, 'partidas': partidas}

#     def contagemGols(self):
#         lista = []
#         for p in range(self.partidas):
#             golsPartida = int(input(f'Quantos gols na {p+1}ª partida: '))
#             lista.append(golsPartida)
#         self.gols['golsPartida'] = lista
#         self.somaGols()
#         self.media()

#     def somaGols(self):
#         self.gols['totalGols'] = sum(self.gols['golsPartida'])

#     def mostraDic(self):
#         return self.gols

#     def media(self):
#         media = self.gols["totalGols"] / self.partidas
#         self.gols ["aproveitamento"] = media 
        
# jogadores = []

# while True:
#     nome = input('Nome do jogador: ')
#     partidas = int(input('Quantas partidas: '))
#     j1 = Jogador(nome, partidas)
#     j1.contagemGols()
#     jogadores.append(j1.mostraDic()) 
#     continuar = input("Cadastrar mais um: ").lower()
#     if continuar == "s":
#         pass
#     else:
#         break

# print (jogadores)

# 4) Crie uma classe que modele uma pessoa:
#    a) Atributos: nome, idade, peso e altura.
#    b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm

class Pessoa():
    def _init_(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        self.idade +=1
        return self.idade
    
    def engordar(self, kg):
        self.peso += kg
        return self.peso
    
    def emagrecer(self, kg):
        self.peso -= kg
        return self.peso
    
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.05
            return self.altura
        else: 
            return self.altura

nome = input('Digite seu nome: ')
idade = int(input('Qual a sua idade? '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
p1 = Pessoa(nome, idade, peso, altura)
print(vars(p1))
novoPeso = int(input('Digite 1- engordou, 2- emagreceu ou 3- não houve alteração. '))
if novoPeso == 1:
        kg = float(input('Quantos kg você engordou? '))
        novoPeso = p1.engordar(kg)
elif novoPeso == 2:
        kg = float(input('Quantos kg você emagreceu? '))
        novoPeso = p1.emagrecer(kg)
else:
        kg = 0

print(p1.envelhecer()) 
print(p1.crescer())
print(novoPeso)
print(vars(p1))