#Contador de letras específicas: El usuario ingresa una palabra y una letra. El programa recorre la
#palabra y cuenta cuántas veces aparece esa letra. Si la letra no aparece, mostrar un mensaje
#indicándolo

def contar_letras(palabra,letra):
    contador = 0
    for caracter in palabra:
        if caracter == letra:
            contador +=1
    
    if contador > 0:
        print(f"la letras {letra} aparece {contador} veces en la palabra {palabra}")
    else:
        print(f"la letra {letra} no aparece la palabra {palabra}")

palabra = input("ingrese una palabra: ")
letra = input("ingrese una letras: ")
contar_letras(palabra, letra)