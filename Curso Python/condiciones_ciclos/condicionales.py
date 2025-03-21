# logico Boolean Booleano
# Verdadero o falso - True / False

# dato = 5 == 5 -- un solo = significa asignacion pero 2 == es igual
# > < ==

print("Ingresa tu nombre")
nombre = input()

if nombre == "Kenneth":
    print("Bienvenido Kenneth")
else:
    print("Que nombre tan peculiar")

print("Terminando programa")


# Condición: bloques if y else
a = 2
b = 1
if a > b:
    print("a es mayor a b")
else:
    print("b es mayor a a")


# Condición: bloques if, elif y else
a = 2
b = 1
if a > b:
    print("a es mayor a b")
elif a == b:
    print("a es igual a b")
else:
    print("b es mayor a a")


# Condición: variables booleanas
a = True
if a:
    print("a es verdadero")
else:
    print("a es falso")


# Condición: instrucción "is" para comparar
lista = [1, 2, 3]
if type(lista) is list:
    print("a es una lista")
else:
    print("a NO es una lista")


# Condición: operador and
a = 10
b = 5
c = 1
if a > b and b > c:
    print("Se cumplen ambas condiciones")


# Condición: operador or
a = 10
b = 5
c = 1
if a > b or b < c:
    print("Se cumple una condición")
