#8. Realizar un programa que obtenga el área del cuadrado.

def areaCuadrado(num1):
    area = num1*num1
    return area

num1 = int(input("Ingrese un lado del cuadrado (m): "))
print(f"""El área del cuadrado es de: {areaCuadrado(num1)}m²""")