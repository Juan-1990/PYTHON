#Solicite el ingreso de una palabra y una letra, 
#luego diga en qué posición está la letra que usted indicó.
palabra = input("Ingrese la palabra: ")
letra = input("Ingrese la letra: ")
posicion = palabra.find(letra) + 1 # se pone + 1 porque python cuenta desde cero
print(f"La posicion de las letras son {posicion}")