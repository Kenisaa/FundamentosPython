def saludar(nombre):
    print("Heya", nombre,)


def celheit(c):
    return (c * 1.8) + 32


print(celheit(15))
print(celheit(20))
print(celheit(25))
print(celheit(45))


def square(side):
    return side * side


print(square(2))

# Funcion para saber si es par o no un numero


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


print(es_par(20))
print(es_par(5))

# Funcion para contar vocales en una palabra


def count_vowels(palabra):
    contador = 0
    vocales = "aeiouAEIOU"

    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador


print(count_vowels("supercalifrajilisticoespialidoso"))
