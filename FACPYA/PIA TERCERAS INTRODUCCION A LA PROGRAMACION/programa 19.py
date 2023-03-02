#19. Realizar un programa que convierta de euros a pesos.

def convertidor_euro_a_mxn(cantidad_euros, precio_pesoMexicano):
    resultado = cantidad_euros*precio_pesoMexicano
    return resultado

cantidad_euros = float(input('Ingrese la cantidad de euros a convertir: '))
precio_pesoMexicano = float(input('Ingrese el precio de el peso dobre el euro: '))

print(f'€{cantidad_euros} en pesos mexicanos son: ${convertidor_euro_a_mxn(cantidad_euros, precio_pesoMexicano):.2f} MXN.')