#18. Realizar un programa que convierta de Pesos a euros.

def convertir_pesos_a_euros(cantidad_pesos, precio_euro):
    resultado = cantidad_pesos/precio_euro
    return resultado

cantidad_pesos = float(input('Ingrese la cantidad de pesos a convertir: '))
precio_euro = float(input('Ingrese el precio del euro en pesos mexicanos: '))

print(f'${cantidad_pesos} en euros son: ${convertir_pesos_a_euros(cantidad_pesos, precio_euro):.2f} euros')