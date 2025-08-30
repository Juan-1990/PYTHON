#cuadrados perfectos: El programa pide un número n 
# y muestra el cuadrado de cada número entre 1 y n. 
# Si el cuadrado es par, agregar la nota '(par)'

def cuadrados_perfectos(n):
    for i in range(1, n + 1):
        cuadrado = i ** 2
        if cuadrado %2 == 0:
            print(f"{i} - 2^ = {cuadrado} (par)")
        else:
            print(f"{i} - 2^ = {cuadrado}")

n = int(input("Ingrese un numero: "))
cuadrados_perfectos(n)