# Escribe un programa que pida un año y determine 
# si es un año bisiesto o no. 
# (Un año es bisiesto si es divisible por 4, pero no por 100, 
# a menos que también sea divisible por 400).

while True:
    anio = int(input("Ingrese el año: "))

    if (anio %4 == 0 and anio %100 != 0) or (anio %400 == 0):
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
        break