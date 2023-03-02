# 17. Realizar un programa que convierta de Pesos a dólares.

def pesos_a_dolares(cantidad_pesos, precio_dolar):
    resultado = cantidad_pesos/precio_dolar
    return resultado

cantidad_pesos = float(input('Ingrese la cantidad de pesos MXN a convertir: '))
precio_dolar = float(input('Ingrese el precio del dólar en pesos: '))

print(f'${cantidad_pesos} son ${pesos_a_dolares(cantidad_pesos, precio_dolar):.2f} dólares.')


