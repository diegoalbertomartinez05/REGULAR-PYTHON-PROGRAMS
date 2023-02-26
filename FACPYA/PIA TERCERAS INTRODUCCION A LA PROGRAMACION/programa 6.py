#6. Realizar un programa que obtenga el promedio de 3 calificaciones.

calificacionesList = []

cantidad = 0

while cantidad<3:
    calificacion=int(input("Ingresa la calificación: "))
    calificacionesList.append(int(calificacion))
    cantidad +=1

cant = sum(calificacionesList)
print(f"""El promedio de las {cantidad} calificaciones es de:  {cant/cantidad}.""")