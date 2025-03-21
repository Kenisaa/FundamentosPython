"""
Guia Practica Valores, Variables y expresiones 
"""
"""
nombre = 'Kenneth'
apellidos = "Callejas"
edad = 24

print(nombre, apellidos, edad)


nombre = 'Kenneth'
apellidos = "Callejas"
edad = edad + 1

print(nombre, apellidos, edad)


nombre = 'Kenneth'
apellidos = "Callejas"
edad3 = edad / 3

print(type(edad3))
"""


print("**********************")
print("****BIENVIENIDO A ****")
print("****LA FERRETERIA ****")
print("***KENNETH CALLEJAS***")
print("***** CC 101019 ******")


pala = 10
espatula = 4
piocha = 6
cuchara = 12
tuerca = 150
escofina = 8


while True:
    print("==========================")
    print("Selecciona la opcion que deseas")
    print("1. Ver articulos en bodega")
    print("2. Ingresar nuevos articulos")
    print("3. Salir")

    respuesta = int(input())

    if respuesta == 1:
        print("Actualmente contamos con:")
        print(f"{pala} Palas, {espatula} Espatulas, {piocha} Piochas, {cuchara} Cucharas, {tuerca} Tuercas, {escofina} Escofinas")
    elif respuesta == 2:
        print("Que articulos quiere agregar?")
        print("1. Pala")
        print("2. Espatula")
        print("3. Piocha")
        print("4. Cuchara")
        print("5. Tuerca")
        print("6. Escofina")

        respuesta2 = int(input())

        if respuesta2 == 1:
            pala += 1
        elif respuesta2 == 2:
            espatula += 1
        elif respuesta2 == 3:
            piocha += 1
        elif respuesta2 == 4:
            cuchara += 1
        elif respuesta2 == 5:
            tuerca += 1
        elif respuesta2 == 6:
            escofina += 1
    elif respuesta == 3:
        print("Saliendo")
        break
1
