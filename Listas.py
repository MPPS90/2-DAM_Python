'''
ESTRUCTURAS DE DATOS:
LISTAS:
Secuencias mutables y ordenadas de elementos indexados por posición

lista=[elemento1, elemento2, elemento3]

FUNCIONES:
print
len
del
del (lista[posicion])->elimina elemento en determinada posición
sorted -> para ordenar listas

Métodos:
append(elemento)->
insert(elemento)->introduce elemento en una posición
remove(elemento)->
pop() -> coge el ultimo elemento insertado en la lista, lo devuelve y lo elimina de la lista
extend(lista2)
index(element)
count(element)
clear()

OPERADORES:
in/not in
> >= < <=
== !=

COPIA LISTAS
= NO COPIA -> PORQUE USA LA REFERENCIA MEMORIA POR TANTO CAMBIA LA ORIGINIAL
.copy()

Ej:
lista = [1,2,3]
lista2 = lista.copy()
'''


#Ejemplos:
lista = [1, 2, 3]
lista2 = lista.copy()
lista3 = [6,5,7]
lista4 = lista.extend(lista3)
print(lista)
print(lista2)
print(lista4)