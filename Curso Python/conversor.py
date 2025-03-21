
print("Bienvenido al conversor de millas a kilometros")
miles = input("Escribe un numero en millas: ")


# print(f"Tipo de datos de millas", {type(miles)})
# Convertir de string a numero

miles = float(miles)
# print(f"Tipo de datos de millas", {type(miles)})

# 1 milla = 1.609 kms
kilometros = miles * 1.609


print(f"\nMillas ingresadas:", miles)
print(f"La conversion es de: {kilometros:.2f} Kms")

# print("kilometros: ",float (kilometros))
