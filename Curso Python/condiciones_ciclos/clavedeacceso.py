"""
Queremos pedirle al usuario una contraseña. Si la contraseña es incorrecta, seguimos pidiéndola 
hasta que el usuario ingrese la contraseña correcta, que es "secreto".
Cuando la contraseña sea correcta, debemos mostrar el mensaje "Acceso concedido".
"""

print("Bienvenido para tener acceso por favor ingresa la contraseña valida")

password = input("ingresa la contraseña: ")  # inicializamos la variable a usar

if password == "secreto":  # comprobamos si la clave ingresada es la correcta
    print("Acceso concedido")  # si es asi, imprimimos
else:
    while password != "secreto":  # si no lo es, entramos en el ciclo hasta que se ingrese la clave correcta
        print("Contraseña incorrecta")
        # pedimos que vuelva a ingrsar la clave en el ciclo
        password = input("Ingresa la contraseña de nuevo: ")
