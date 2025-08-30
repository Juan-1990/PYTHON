# Suma de positivos y negativos: 
# El programa pide 5 números enteros al usuario y debe indicar
# cuántos son positivos, cuántos son negativos y cuántos son iguales a cero.

def contar_numeros(positivo, negativo, cero):
    for i in range(5):
        numero = int(input("Ingrese un numero entero: "))
        if numero > 0:
            print(f"el numero {numero} es positivo")
        elif numero < 0:
            print(f"el numero {numero} es negativo")
        else: 
            print(f"el numero {numero} es igual a cero")

positivo = 0
negativo = 0
cero = 0
contar_numeros(positivo, negativo, cero)