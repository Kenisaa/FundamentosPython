# Suma de numeros positivos

print("Bienvenido, por favor ingresa solamente numeros positivos")
print("Si ingresas un numero negativo, el programa se terminara")

# inicializamos las variables que utilizaremos
numero = int(input("Ingresa un numero: "))
suma = 0

# Friendly reminder: podemos usar if antes del while, eso nos permite verificar una condicion antes de que el ciclo se ejecute

if numero < 0:      # ponemos la condicion  que si el numero que ingresamos es menor a 0 imprime el mensaje, pero si no lo es ejecuta el else
    print("El numero que ingresaste no es positivo.")
else:
    while numero >= 0:  # si el numero es mayor o igual a 0 pues ejecuta el ciclo
        suma += numero
        numero = int(input("ingresa otro numero: "))

print("La suma total de los numero positivos es igual a : ", suma)
