'''
Sin utilizar las funciones index, count, max o sum, realizar los siguientes ejercicios
* Crear una lista aleatoria no ordenada de 50 números entre 1 y 20:
* Implementar funciones que realicen asl siguientes operaciones:
    * buscar(lista, numero): buscar en una lista un número. Si lo encuentra, debe indicar su posición en la lista, en otro caso devolverá -1
    * contar(lista, numero): devuelve el número de veces que aparece el número buscado.
    * contar_maximo(lista): calcula el número máximo en la lista y devuelva cuántas veces aparece.
    * calcular_media(lista): calcular la media de todos los números en la lista.
    * inversa: devolver lista inversa a la dada, donde el primer elemento sea el último de la lista original, el segundo elemento sea el penúltimo de la lista original, y así sucesivamente.
    * insertar(lista, numero, posicion): inserta un número en la lista en la posición indicada y devuelve la nueva lista
    * insertar(lista, numero, posicion): inserta un número en la propia lista
'''
import random

# 1. Crear una lista aleatoria no ordenada de 50 números entre 1 y 20:
lista = []
for i in range(50):
    lista.append(random.randint(1,21))  # aqui relleno la lista con los randoms, si lo declaro arriba con un random tendría que poner entonces abajo range(49) porque la de arriba ya lo cuenta como 1
print("la longitud es:", len(lista))

for indice in range(0, len(lista)):  #for normal
    print(lista[indice])

'''
for indice in lista
    print(lista[indice])   -> for each ->aquí cada indice es el valor del array no la posición por eso lista[indice] sería lista[valordelalista] no lista[posicion]
'''


# 2. Implementar funciones que realicen asl siguientes operaciones:
'''
# 1.Buscar en la lista:
def buscar_num(lista, numero):
    encontrado = False
    for i in range(0, len(lista)):
        if lista[i] == numero:
            encontrado = True
            print(i)
    if not encontrado:
        return print(-1)
        

buscar_num(lista, int(input("Ingrese numero")))
    
'''



#2 contar(lista, numero): devuelve el número de veces que aparece el número buscado.
def contar_num(lista, numero):
    contador = 0
    encontrado = False
    for i in range(0, len(lista)):
        if lista[i] == numero:
            encontrado = True
            contador +=1
    print(contador)
    if not encontrado:
        return print(-1)


contar_num(lista, int(input("Ingrese número")))