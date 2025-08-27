#Capture el salario de una persona y determine si dicho salario es integral.
salario = float(input("Ingrese el salario: "))
smmlv = float(input("Ingrese el SMMLV: "))
if salario <= 0 or smmlv <= 0:
    print("Valores incorrectos")
else:
    print("Salario integral" if salario >= 13 * smmlv else "Salario no integral" )