#Capture el sexo de una persona y salude a 
# dicha de persona de manera adecuada según su sexo.

sexo = input("Ingrese el sexo (M/F/Otro): ")
nombre = input("Ingrese el nombre: ")

if sexo in ("m", "masculino", "h", "hombre" ):
    print(f"Hola, Señor {nombre or 'Usuario'}. ")
elif sexo in ("f", "femenino", "mujer" ):
    print(f"Hola, señora {nombre or 'Usuario'}. ")
else:
    print(f"Hola, {nombre or 'Usuario'}")
     