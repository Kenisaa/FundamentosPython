import math


apellido = "Callejas"

"""
def funcion():      # Definimos la funcion sin parametros
    print("Mi primera funcion")  # Le decimos que haga una impresion
    nombre = "Isaias"       # Definimos o inicializamos la variable nombre
    print(f"Mi nombre es {nombre} {apellido}")  # Imprimimos las variables


print(funcion())
"""

"""
# Funcion Argumentos

def perimetro_cuadrado(lado, unidades):
    perimetro = lado * 4
    # podemos usar return en vez de print y eso no retorna el none
    return f"El perimetro es {perimetro} {unidades}"


print(perimetro_cuadrado(50, "cms"))

"""

"""

# Funcion para sacar area de un cuadrado

def area_cuadrado(base, altura, uni):
    area = base * altura
    return f"El area del cuadrado es {area} {uni}"


print(area_cuadrado(12, 12, "cms"))

"""


"""
# Funcion para sacar el area de un triangulo

def area_triangulo(base, altura, unidades):
    area = base * altura / 2
    return f"El area del triangulo es {area} {unidades}"


print(area_triangulo(10, 5, "cms"))

"""

# Funcion para sacar el area de un circulo
# Formula:  Area = pi*r2


def area_circulo(radio, unidades):
    area = math.pi * radio**2
    return f"El area del circulo es {area} {unidades}"


print(area_circulo(4, "cms"))


#
