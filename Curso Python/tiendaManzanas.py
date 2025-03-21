print("*****************************")
print("****   BIENVIENIDO A    *****")
print("*** LA TIENDA DE MANZANAS ***")
print("*****************************")

manzanas = 20

print("Ingrese su nombre por favor:")
nombre = input()

print("Hola, ", nombre, "actualmente contamos con un total de",
      manzanas, "manzanas, cada una vale $5")


print("Cuantas manzanas quisiera comprar?")
compra = input()

# print(type(compra))
compra = int(compra)  # hacemos conversion de variable a int


totalVenta = compra * 5

print("El total por la compra de ", compra, "es de: ", totalVenta, "Dolares")


# print(type(compra))


totalManzanas = manzanas - compra

print("Ahora el total de manzanas es: ", totalManzanas)
