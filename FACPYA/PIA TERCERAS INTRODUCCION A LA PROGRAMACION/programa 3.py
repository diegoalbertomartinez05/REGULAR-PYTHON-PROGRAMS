#3. Realizar un programa que pida 2 números al usuario y sume dichos números.

def sumaNumeros(numero1,numero2):
    suma=numero1+numero2
    return suma

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

print("La suma de ", numero1, "+",numero2, "es: ", sumaNumeros(numero1, numero2))

