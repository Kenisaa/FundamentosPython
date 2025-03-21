nombres = ["Kenneth", "Moises", "Christopher"]
lenguajes = ["Python", "Java", "JavaScript", "C#", "C++", "PHP"]
frontend = ["html", "css",]
# 0 Kenneth 1 Moises 2 Christopher
# 0 = Python, 1 = Java, 2 = JavaScript

# Las listas pueden tener elementos de diferentes tipos
lista = ["Hola", 2, True, 5.5,]
print(type(lista))

# Para ver un indice de la lista especificamos el indice
print(nombres[2])

# Usamos indices negativos para obtener las posiciones de las listas desde el ultimo hasta el primero
print(lenguajes[-1])

# Las listas son modificables
nombres[0] = "Isaias"
print(nombres)

# Podemos ver la longitud de la lista con la funcion len()
print(len(nombres))

# Para ver que la variable es una lista usamos type
print(type(nombres))

# con append podemos agregar elementos a la lista al final
nombres.append("Jose")
print(len(nombres))

# Podemos quitar elementos de las listas con remove
nombres.remove("Isaias")
print(nombres)

# Podemos ver si un elemento se encuentra en una lista
print("Isaias" in nombres)
print(lenguajes)

# Usamos slicing para obtener una sublista
print(lenguajes[1:4])  # el primero es inclusivo y el segundo es el exclusivo

# Listas anidadas
todo = [frontend, lenguajes, "NodeJs", "astro"]
print(todo)
print(todo[0][0])

# Modificamos una posicion asignandole un nuevo valor
lenguajes[0] = "Dart"
print(lenguajes)

# append() permite añadir elementos al final de la lista
lenguajes.append("Python")
print(lenguajes)

# extend() permite unir dos listas
otros_lenguajes = ["Kotlin", "Swift", "Rust"]
lenguajes.extend(otros_lenguajes)
print(lenguajes)


# Eliminacion de elementos de la lista
lenguajes.pop(2)
# lenguajes.pop("Python")  # Da error por que espera un entero
print(lenguajes)
