#9. Realizar un programa que calcule el perímetro de un cuadrado.

ladosCuadrado=[]
cantidad=0
cantidadLado=0

while cantidad<4:
    cantidad+=1
    cantidadLado+=1
    lado=int(input(f"""Ingrese el lado {cantidadLado}: """))
    ladosCuadrado.append(int(lado))

resultado = sum(ladosCuadrado)
print(f"""El perimetro de el cuadrado es de {resultado}m""")