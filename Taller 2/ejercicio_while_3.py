# Escribe un programa que presente un menú con opciones 
# para realizar una operación matemática 
# (suma, resta, multiplicación o división) entre dos números. 
# El programa debe repetirse hasta que el usuario elija salir.

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingresa la opción: ")
    if opcion == "5":
        break

    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa un número: "))

    n1 = num1 + num2
    n2 = num1 - num2
    n3 = num1 * num2
    n4 = num1 / num2

    if opcion == "1":
        print(f"Resultado: {n1}")
    elif opcion == "2":
        print(f"Resultado: {n2}")
    elif opcion == "3":
        print(f"Resultado: {n3}")
    elif opcion == "4":
        print(f"Resultado: {n4}")
