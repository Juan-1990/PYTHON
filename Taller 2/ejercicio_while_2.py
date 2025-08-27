# Escribe un programa que pida un número entero 
# positivo n y calcule la suma de todos los números pares entre 1 y n.

n = int(input("Ingrese un numero positivo: "))
suma = 0
i = 2
while i <= n:
    suma = n + i 
    print(f"{n} + {i} = {suma}")
    i += 2