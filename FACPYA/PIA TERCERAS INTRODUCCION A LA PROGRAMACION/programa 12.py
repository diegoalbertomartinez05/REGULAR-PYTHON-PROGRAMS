#12. Realizar un programa que calcule el área de un rectángulo.

def areaRectangulo(base, altura):
    area = base*altura
    return area

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

print(f"""
El área del rectángulo es de: {areaRectangulo(base, altura)}
""")