nombres = ["Kenneth", "Moises", "Christopher", "Juan", "Alfredo", "Carlos"]
print(nombres)


# Podemos iterar con listas para

# Podemos usar la funcion enumerate() Para poder ver los indices de los elementos de la lista

for i, nombre in enumerate(nombres):
    print(f"Se inscribio {nombre} en la lista con el indice {i}")

print("Bienvenidos a la fiesta", nombres[:3])
print("Lo sentimos", nombres[3:])
