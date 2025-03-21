import random
nombre = "Kenneth"

print("Longitud del nombre Kenneth", len(nombre))

# Valor absoluto funcion abs

print(abs(-10))


# funcion random, importar libreria ramdom


aleatorio = random.randint(1, 100)
print(aleatorio)


# Funcion saludar, sumar

def saludar_sumar(nombre, num1, num2=0):
    print("Saludos", nombre)
    print("Resultado de la suma", num1 + num2)


saludar_sumar('Kenneth', 10, 30)
saludar_sumar('Isaias', 30)
saludar_sumar('Bessy', 1920, 85)
