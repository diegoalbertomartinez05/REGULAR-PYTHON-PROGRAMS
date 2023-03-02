# 15. Realizar un programa que convierta de dólares a pesos.

def resultadoCambio(dolares, cambio_peso):
    resultado = dolares*cambio_peso
    return resultado

dolares = int(input('ingrese la cantidad de dólares a convertir: '))
cambio_peso = float(input('Ingrese el cambio de dolar sobre peso mexicano (USD/MXN): '))

print(f'${dolares} en pesos son: {resultadoCambio(dolares,cambio_peso)} MXN.')