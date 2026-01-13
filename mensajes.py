def mensaje_imc(imc):
    if imc < 18.5:
        return "Estás por debajo del peso ideal 😬"
    elif 18.5 <= imc < 25:
        return "Tienes un peso normal 👍"
    elif 25 <= imc < 30:
        return "Tienes sobrepeso ⚠️"
    else:
        return "Obesidad 🚨 ¡Cuidado!"