#11. Realizar un programa que calcule el perímetro de un círculo.

def calcuPerimetroDiametro(diametro):
    perimetro = 3.14*diametro
    return perimetro

def calcuPerimetroRadio(radio):
    perimetro = 3.14*(radio*2)
    return perimetro

dato = int(input("""
Calcular perimetro de un círculo, ¿Qué dato tiene del círculo)
Presione 1. para diametro
Presione 2. para radio
Ingrese número: 
"""))

if dato == 1:
    diametro = float(input("Ingrese el diámetro del círculo: "))
    print(f"""
PERIMETRO
Fórmula = π*Diámetro
Diámetro = {diametro}
Pi = 3.14

El resultado es: {calcuPerimetroDiametro(diametro)}
""")

elif dato == 2:
    radio = float(input("Ingrese el radio del cículo: "))
    print(f"""
PERIMETRO
Fórmula = π*Diámetro
Fórmula para díametro = r*2
Pi = 3.14

El resulado es: {calcuPerimetroRadio(radio)}
""")