# SERIE DE FIBONACCI
# expresion matematica f(n) = f(n -1) + f(n -2)
n1 = 0
n2 = 1  # n2 es el numero 2 posiciones atras
n = 0

print(n1)
print(n2)
while n < 10:
    suma = n1 + n2  # sunmanos los dos primeros numeros
    print(suma)  # imprimios el resultado de la suma

    n1 = n2  # actualizamos el primer numero con el valor de n2 del inicio
    n2 = suma  # actualizamos con el valor de la suma

    n += 1    # hacemos la suma en el ciclo para que se efectue la suma
