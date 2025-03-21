import random


def tirar_dados():
    return random.randint(2, 12)


# print("Tirada de dados: ", tirar_dados())


def pedir_respuesta():
    print("Ingresa tu prediccion")
    print("1. Impar")
    print("2. Par ")
    print("3. Salir del juego")

    return int(input())


def imprimir_resultado(numero, prediccion):
    # Not
    # Saber si un numero es par o impar
    # dividir entre 2 y si el remanente es 0, es par si es 1, es impar
    # Resultado = 5/2: Resultado seria 2 con remanente 1
    # Resultado = 6/2: Resultado seria 3, con remanente 0
    es_par = numero % 2 == 0
    # es_par, Prediccion = 1: Gane
    # no es_par, Prediccion = 2: Gane
    # Perdi

    if not es_par and prediccion == 1:
        print("Ganaste! Número de los dados es:", numero)
    elif es_par and prediccion == 2:
        print("Ganaste! Número de los dados es:", numero)
    else:
        print("Perdiste! Número de los dados es:", numero)


# Buscar numeros intermitentes

while True:
    numero = tirar_dados()
    prediccion = pedir_respuesta()
    if prediccion == 3:
        break
    imprimir_resultado(numero, prediccion)

print("Gracias por jugar")
