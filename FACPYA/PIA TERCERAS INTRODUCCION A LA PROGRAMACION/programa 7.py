#7. Realizar un programa que obtenga el cuadrado de un número.

def resultCuadrado(num1):
    resultado=num1*num1
    return resultado

num1=int(input("Ingresa un número: "))

print(f"""El cuadrado de {num1} es {resultCuadrado(num1)}""")