#1.	Escribe un programa que pida un número 
# entero y muestre su tabla de multiplicar del 1 al 10.

numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
