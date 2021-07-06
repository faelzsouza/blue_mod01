class Tempo:
    
    def __init__(self, hora = 1):
        self.dia = 1
        self.hora = hora
        
    def passarHora(self, valor):
        self.hora += valor
        return self.hora

    def avancarDia(self):
        self.dia += 1 
