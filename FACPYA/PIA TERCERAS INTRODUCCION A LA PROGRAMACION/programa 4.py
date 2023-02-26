#4. Realizar un programa que pida 2 números al usuario y reste dichos números.

def restaNumeros(numero1,numero2):
    resta = numero1-numero2
    return resta

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

print("La resta de ", numero1, "-",numero2, "es: ", restaNumeros(numero1, numero2))