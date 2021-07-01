# Exercício de Fixação

# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro.
# iii. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos: 
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
# foi colocada no veículo.
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
# a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba. 
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
    def __init__(self, tipoCombustivel = '', valorLitro = 0, quantidadeCombustivel = 0):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self, valorAbastece):
        quantidadeAbastece = valorAbastece / self.valorLitro
        self.quantidadeCombustivel -= quantidadeAbastece
        print(f'Seu veículo foi abastecido com {quantidadeAbastece:.2f}L de combustível.')
        print()
        print(f'Quantidade de combustível na bomba: {self.quantidadeCombustivel:.2f}L')
    
    def abastecerPorLitro(self, litroAbastece):
        quantidadeAbastece = litroAbastece * self.valorLitro
        self.quantidadeCombustivel -= litroAbastece
        print(f'O total é R${quantidadeAbastece:.2f}.')
        print()
        print(f'Quantidade de combustível na bomba: {self.quantidadeCombustivel:.2f}L')
    
    def alterarValor(self, valor):
        self.valorLitro = valor
    
    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo
    
    def alterarQuantidadeCombustivel(self, quantidade):
        self.quantidadeCombustivel = quantidade

bomba1 = BombaCombustivel('Gasolina', 5.9, 50)

bomba1.abastecerPorValor(40)
bomba1.abastecerPorLitro(10)