# Actividad

print("*********************************")
print("*                               *")
print("* Bienvenido a la Cafeteria UFG *")
print("*                               *")
print("*********************************")


precio_dolar = 1
precio_colon = 8.75
tostadas = 25
# 1 Dolar equivale 8.75 de colon


def bienvenida():
    print(f"\nGracias por visitarnos {nombre} con número de carné: {carnet}")


def mostrar_inventario():

    print("Actualmente contamos con: ")
    print(f"{tostadas} Tostadas cada una al valor de $1.00 (8.75 de colon) ")


def mostrar_menu():
    print("")
    print("===============================\n")
    print("Selecciona la opcion que deseas\n")
    print("1: Conocer cuantas tostadas tiene la tienda")
    print("2: Comprar un tostadal")
    print("3: Salir\n")


def comprar_tostadas():
    global tostadas  # Para modificar el inventario globalmente
    while True:
        try:
            tostadas_compra = int(input("¿Cuántas tostadas quieres comprar? "))
            if tostadas_compra < 1:
                print("Debes comprar al menos una tostada.")
            elif tostadas_compra > tostadas:
                print("No tenemos suficientes tostadas en inventario.")
            else:
                total_dolar = tostadas_compra * precio_dolar
                total_colon = tostadas_compra * precio_colon
                tostadas -= tostadas_compra  # Restar del inventario
                print(f"Has comprado {tostadas_compra} tostadas.")
                print(
                    f"Total a pagar: ${total_dolar:.2f} ({total_colon:.2f} colones)")
                break  # Salir del bucle después de una compra válida
        except ValueError:
            print("Por favor, ingresa un número válido.")


nombre = input("\nPor favor, ingrese su nombre: ")
carnet = input("Por favor, ingrese su carné: ")

bienvenida()
while True:
    mostrar_menu()
    respuesta = int(input())
    if respuesta == 1:
        print(nombre)
        mostrar_inventario()
    elif respuesta == 2:
        print(nombre)
        comprar_tostadas()
    elif respuesta == 3:
        print(f"Nos quedan {tostadas} tostadas disponibles.")
        print("Te esperamos pronto!!")
        break
