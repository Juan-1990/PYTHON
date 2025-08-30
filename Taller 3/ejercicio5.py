# Clasificación de notas: Un profesor ingresa 5 notas (de 0 a 5). 
# El programa debe mostrar cada nota y clasificarla como Aprobada o Reprobada. 
# Al final, mostrar el total de aprobadas y reprobadas

def clasificar_notas(aprobadas, reprobadas):
    
    for i in range(5):
        nota = float(input(f"Ingresa la nota {i+1} (0 a 5): "))
        if nota >= 3.0:
            print(f"Su nota es {nota} aprobada")
            aprobadas += 1
        else:
            print(f"Su nota es {nota} reprobada")
            reprobadas += 1

aprobadas = 0
reprobadas = 0

clasificar_notas(aprobadas, reprobadas)