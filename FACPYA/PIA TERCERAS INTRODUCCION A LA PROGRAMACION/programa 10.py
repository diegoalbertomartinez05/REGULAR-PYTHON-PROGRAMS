#10. Realizar un programa que calcule el área de un círculo.

def areaCirculo(radio):
    area=3.14*(radio*radio)
    return area

radio =float(input("Ingrese el radio del círculo: "))
print(f"""El área del círculo es: {areaCirculo(radio)}""")