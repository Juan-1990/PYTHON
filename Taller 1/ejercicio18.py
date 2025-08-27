#Capture dos números y determine cuál de ellos es el mayor, cual el menor o si son iguales.
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if num1 > num2:
    print(f"El mayor es: {num1}")
    print(f"El menor es: {num2}")
elif num2 > num1:
    print(f"EL mayor es: {num2}")
    print(f"El menor es: {num1}")
else:
    print("Ambos numeros son iguales")