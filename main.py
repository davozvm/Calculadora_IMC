class CalculadoraPeso:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.imc = self.calcular_imc()
    
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
    
    def mensaje(self):
        if self.imc < 18.5:
            return "Estás por debajo del peso ideal 😬"
        elif 18.5 <= self.imc < 25:
            return "Tienes un peso normal 👍"
        elif 25 <= self.imc < 30:
            return "Tienes sobrepeso ⚠️"
        else:
            return "Obesidad 🚨 ¡Cuidado!"

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

calculadora = CalculadoraPeso(peso, altura)
print(f"Tu IMC es: {calculadora.imc:.2f}")
print(calculadora.mensaje())