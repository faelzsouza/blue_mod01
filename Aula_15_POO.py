# 1.a) Crie uma classe pessoa com os seguintes atributos: nome,
# sobrenome e idade.

# class Pessoa():
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade

# # 1.b) Acrescente a classe criada um método para mostrar os dados de
# # uma pessoa.

# class Pessoa():
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade
    
#     def printando(self):
#         print(self.nome, self.sobrenome, self.idade)

# # 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e
# # métodos.

# class Pessoa():
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade
    
#     def printando(self):
#         print(self.nome, self.sobrenome, self.idade)

# umapessoa = Pessoa('Fulano', 'Silva', 25)

# umapessoa.printando()

# 2) Crie uma classe chamada Conta para simular as operações de
# uma conta corrente. Sua classe deverá ter os atributos Titular e
# Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
# Conta e teste os atributos e métodos implementados.

# class Conta():
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
    
#     def sacar(self, valor):
#         print(f'Olá {self.titular}, seu saldo é R${self.saldo:.2f}')
#         if valor <= self.saldo:
#             self.saldo -= valor
#             print(f'Seu novo saldo é R${self.saldo:.2f}')
#         else:
#             print(f'{self.titular}, você não tem saldo suficiente para esse saque!')
    
#     def depositar(self, valor):
#         print(f'Olá {self.titular}, seu saldo é R${self.saldo:.2f}')
        
#         self.saldo += valor
#         print(f'Seu novo saldo é R${self.saldo:.2f}')

# a = Conta('Rafael', 1000)

# valor = float(input('Quanto deseja sacar? R$'))
# a.sacar(valor)

# valor = float(input('Quanto deseja depositar? R$'))
# a.depositar(valor)
