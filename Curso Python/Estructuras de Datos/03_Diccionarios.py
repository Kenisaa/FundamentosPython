# Declarar un diccionario

lenguaje = {
    "nombre": "python",
    "creador": "Guido Van Rossum"
}
print(lenguaje)

# añadir nuevas llaves y valores

lenguaje["año_lanzamiento"] = 1991
print(lenguaje)


# Sobreescribir el valor de una llave
lenguaje["año_lanzamiento"] = 1999
print(lenguaje)

lenguaje["Caracteristica"] = "sencillo", "facil", "genial"
print(lenguaje)

# items(), retorna una lista de tuplas (llave, valor)
print(lenguaje.items())
