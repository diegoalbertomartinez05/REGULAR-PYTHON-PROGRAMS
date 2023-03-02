# 16. Realizar un programa que convierta de dólares a euros.

def converDivisas(cantDolares, precio_euro):
    resultado = cantDolares * precio_euro
    return resultado

cantDolares = float(input('Ingrese la cantidad de dolares a convertir: '))
precio_euro = float(input('Ingrese el precio del dólar sobre el euro (USD/EUR): '))

print(converDivisas(cantDolares, precio_euro))

