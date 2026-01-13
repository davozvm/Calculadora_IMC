class CalculadoraPeso:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.imc = self.calcular_imc()
    
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)