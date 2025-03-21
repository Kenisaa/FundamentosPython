# Crea un programa que cuente hacia atrás desde un número que el usuario ingrese hasta llegar a 0. Al llegar a 0, debe imprimir "¡Se acabó!".


numero = int(input("Ingresa un numero para contas hacia atras: "))


while numero > 0:
    print(numero)
    numero -= 1
