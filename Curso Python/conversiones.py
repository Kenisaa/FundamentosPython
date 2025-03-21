print("Bienvenido, que quieres convertir?")

print("1. Fahrenheit a Celsius")
print("2. Millas a Kilometros")

seleccion = int(input())

if seleccion == 1:
    print("Selecciono convertir Fahrenheit a Celsius")
    print("ingrese los grados que quiere convertir")
    fahrenheit = float(input())
    celsius = (fahrenheit - 32) * 5 / 9
    print("La conversion es:", celsius, "C")

elif seleccion == 2:
    print("Selecciono convertir Millas a Kilometros")
    print("ingrese por favor, las millas a convertir")
    miles = float(input())
    kilometros = miles * 1.609
    print("La conversion es de:", kilometros, "Kms")


print("Fin del programa")
