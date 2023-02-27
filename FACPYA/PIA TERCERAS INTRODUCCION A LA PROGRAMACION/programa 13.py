#13. Realizar un programa que calcule el área de un triángulo.

def areaTriangulo(base, altura):
    area = (base*altura)/2
    return area

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

print(f"""
El área del triángulo es: {areaTriangulo(base, altura)}
""")