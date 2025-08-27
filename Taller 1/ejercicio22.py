# Capture tres números y determine cuál de ellos es el mayor, 
# cual el menor y cuál es el del medio.
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
nums = sorted([a, b, c])
print(f"Menor = {nums[0]}, Medio = {nums[1]}, Mayor = {nums[2]}")