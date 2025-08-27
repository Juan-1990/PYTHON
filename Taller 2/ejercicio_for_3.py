#Escribe un programa que presente un menú con opciones 
# para realizar una operación matemática 
# (suma, resta, multiplicación o división) entre dos números. 
# El programa debe repetirse hasta que el usuario elija salir.

for _ in range(999999):
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    opcion = input("Elija una Opcion: ")

    if opcion == "5":
        break

    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese un numero: "))

    n1 = num1 + num2
    n2 = num1 - num2
    n3 = num1 * num2
    n4 = num1 / num2

    if opcion == "1":
        print(f"Resultado es: {num1} + {num2} = {n1}")
    elif opcion == "2":
        print(f"Resultado es: {num1} - {num2} = {n2}")
    elif opcion == "3":
        print(f"Resultado es: {num1} * {num2} = {n3}")
    elif opcion == "4":
        print(f"Resultado es: {num1} / {num2} = {n4}")