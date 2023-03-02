# 20. Realizar un programa que convierta de euros a dólares.

def convertidor_euroAdolar(cantidad_euros, precio_dolar):
    resultado = cantidad_euros*precio_dolar
    return resultado

cantidad_euros = float(input('Ingrese la cantidad de euros a convertir: '))
precio_dolar = float(input('Ingrese el cambio de euro a dolar (EUR/USD): '))

print(f'€{cantidad_euros} son ${convertidor_euroAdolar(cantidad_euros, precio_dolar):.2f} USD')