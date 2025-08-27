# Escribe un programa que pida un número entero 
# positivo n y calcule la suma de todos los números pares entre 1 y n.
n = int(input("Ingrese un numero entero positivo: "))

suma = 0

for i in range(2, n+1, 2):
    print(f"suma = suma + {i}")