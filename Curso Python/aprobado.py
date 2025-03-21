print("*****************************")
print("*****   BIENVIENIDO     *****")
print("***CALCULAREMOS TUS NOTAS ***")
print("*****************************\n")
print("Quieres saber si has aprobado el ciclo?")
print("Por favor, ingresa las 4 notas del ciclo")

firstGrade = float(input("Primera nota:"))
secondGrade = float(input("Segunda nota:"))
thirdGrade = float(input("Tercera nota:"))
fourthGrade = float(input("Cuarta nota:"))

average = float(firstGrade + secondGrade + thirdGrade + fourthGrade) / 4

# print(type(average)) impresion de variable para ver el tipo de dato

if average >= 7.00:
    print("Excelente, has aprobado el ciclo con:", average)
else:
    print("Lastimosamente, no has aprobado el ciclo, lo dejaste con:", average)

print("Termina el programa")
