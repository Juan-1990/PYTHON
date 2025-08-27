# Escribe un programa que pida un número 
# entero y muestre su tabla de multiplicar del 1 al 10.

numero = int(input("Ingrese el numero entero: "))
i = 1
while i <= 10:
    num = numero * i
    print(f"{numero} x {i} = {num}")
    i += 1