'''
Desarrolla un programa que implemente el juego del Ahorcado.
El objetivo es adivinar una palabra secreta letra por letra, dentro de un número limitado de intentos.
La palabra secreta se obtendrá aleatoriamente de una lista en la que habrá varias posibles palabras.
En cada intento, el jugador ingresará una letra.
El programa mostrará la palabra con las letras adivinadas reveladas y las letras no adivinadas como guiones bajos (_).
El juego termina cuando el jugador adivina la palabra completa o se queda sin intentos.
'''
import random


def ahorcado(a):
    intentos = 6
    palabras = ["salon", "habitacion", "baño", "cocina"]
    palabraElegida = palabras[random.randint(0,len(palabras))]

    while(intentos>0):
        i = 0
        letra=input("Ingresa una letra")
        if letra == palabraElegida[i]:
            i= i+1





    return