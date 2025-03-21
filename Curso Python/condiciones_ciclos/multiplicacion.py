# Crea un programa que pida al usuario un número y luego lo multiplique por 2 repetidamente
#  hasta que el resultado sea mayor o igual a 1000. Imprime el resultado en cada paso.


numero = int(input(
    "Por favor, ingresa un numero para que se multiplique po 2 hasta llegar a 1000: "))

resultado = numero

while resultado < 1000:
    print(resultado)
    resultado *= 2
