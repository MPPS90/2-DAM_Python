'''Escribir una función que, dado un dígito entre 1 y 7, devuelva dos resultados: el día de la semana correspondiente y
el día siguiente. Ambos días deben ser devueltos como cadenas de texto, por ejemplo, "lunes", "martes", "miércoles", etc.
Los nombres de los días de la semana deben estar almacenados en una tupla.'''

def diaSemana(n):
    while(n < 1 or n > 7):
        n = input("El número debe ser entre 1 y 7 ")

    dias=["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    if n ==7:
        return print(dias[n - 1], dias[0])
    else:
        return print(dias[n - 1], dias[n])

diaSemana(7)

