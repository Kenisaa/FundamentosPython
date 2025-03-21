print("*****************************")
print("***    BIENVIENIDO A      ***")
print("*** LA TIENDA DE MASCOTAS ***")
print("*****************************\n")


num_perros = 10
num_gatos = 8
num_pajaros = 25


nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")

# Concatenacion

nombre_completo = nombre + " " + apellido

print("Gracias por visitarnos", nombre_completo)


def mostrar_menu():
    print("")
    print("===============================\n")
    print("Selecciona la opcion que deseas\n")
    print("1: Conocer cuantos animales tiene la tienda")
    print("2: Comprar un animal")
    print("3: Salir")


def mostrar_inventario():
    print("Actualmente contamos con:")
    # usamos el formato(f-string) para evitar que el codigo se divida en varias lineas
    print(f"{num_perros} Perros, {num_gatos} Gatos, {num_pajaros} Pajaros")
    totalAnimales = num_perros + num_gatos + num_pajaros
    print("El total de los animales es: ", totalAnimales)


def comprar_animal():
    carrito = []

    while True:
        print("Que animal deseas comprar?")
        print("Escribe F para terminar la lista")

        animal = input()
        if animal == "F" or animal == "f":
            break
        if animal not in carrito:
            carrito.append(animal)
        else:
            print("Ese animal ya se encuentra en tu carrito")
        print("Has comprado un", animal)
    print("El contenido de tu carrito es")
    for animal in carrito:
        print("   ", animal)


while True:
    mostrar_menu()
    respuesta = int(input())
    print(nombre, apellido)
    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_animal()
    elif respuesta == 3:
        print("Saliendo")
        break
