nombre = input("Escribe tu nombre:")
edad = int(input("Escribe tu edad:"))


# elif podemos poner todos los elif que deseemos hasta que no se cumplan los 2 entonces se ejecutara el else
if nombre == "Kenneth" and edad > 18:
    print("Hola Kenneth, eres mayor de edad")
elif nombre == "Isaias" and edad <= 18:
    print("Que bonito nombre, Isaias pero eres menor")
else:
    print("No se quien eres")


# Operadores Logicos
# and (y) podemos colocarlo despues de nuestra expresion, para agregar otra expresion - todas las expresiones tienen que ser true
# or (o) solo revisa que 1 de las expresiones sea true
# < > <= >=
