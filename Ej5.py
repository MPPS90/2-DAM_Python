'''

Realiza un programa en el que se introduzcan las notas de los alumnos de la clase.
Las notas serán números enteros
La entrada de datos finalizará con un número negativo
Realizar una función que muestre una gráfica con las notas y las veces que se repiten.
¿Cuál es la nota que más se repite?

'''


def notasAlumnos(n):
    notas = []
    while (n > 0):
        notas.append(n)
        n = int(input("Ingresa la nota: "))
    for i in range(0, 11):
        print(i, ":", end="")
        for j in range(0, len(notas) - 1):
            if notas[j] == i:
                print("*", end="")
        print(" ")


notasAlumnos(int(input("Ingrese la nota: ")))
