# Capture el peso y la altura de una persona, 
# calcule el IMC y determine si dicha persona está en sobrepeso, 
# peso normal o desnutrición.
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en metros: "))
if peso <= 0 or altura <= 0:
    print("Peso y altura deben ser positivos.")
else:
    imc = peso / (altura ** 2)
    if imc < 18.5:
        cat = "Desnutrición"
    elif imc < 25:
        cat = "Peso normal"
    else:
        cat = "Sobrepeso"
    print(f"IMC = {imc:.2f}, Categoría = {cat}")