#14. Realizar un programa que calcule el porcentaje de una cantidad.

def resultPorcentaje(cantidad, porcentaje):
    resultado = (cantidad*porcentaje)/100
    return resultado

cantidad = int(input('Ingrese la cantidad a sacar porcentaje: '))
porcentaje = int(input('Ingrese el porcentaje a sacar: '))

print(f'el {porcentaje}% de {cantidad} es: {resultPorcentaje(cantidad, porcentaje)}')