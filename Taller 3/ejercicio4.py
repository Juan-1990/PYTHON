# Números primos en un rango: El usuario ingresa un número 
# límite y el programa imprime todos los
# números primos entre 1 y ese límite

def numeros_primos(limite):
    i = 2
    for num in range(2, limite + 1):
        es_primo = True
        for divisor in range( 2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            print(num)
limite = int(input("Ingrese un número límite: "))
print(f"Números primos entre 1 y y {limite}")
numeros_primos(limite)