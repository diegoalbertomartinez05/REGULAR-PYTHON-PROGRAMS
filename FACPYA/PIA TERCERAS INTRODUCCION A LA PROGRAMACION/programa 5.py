#5. Realizar un programa que pida 2 números al usuario y multiplique dichos números.

def multiplicaNumeros(numero1,numero2):
    multiplicacion = numero1*numero2
    return multiplicacion

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese un número: "))

print("La multiplicación de ", numero1, "x",numero2, "es: ", multiplicaNumeros(numero1, numero2))
