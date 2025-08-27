#Cree un programa que pida un ángulo y regrese el seno, 
# el coseno y la tangente del mismo. Pista: use la clase “math”.
import math
angulo_grados = float(input("Ingrese un angulo en grados: "))
angulo_radianes = math.radians(angulo_grados)

seno = math.sin(angulo_radianes)
coseno = math.cos(angulo_radianes)
tangente = math.tan(angulo_radianes)

print(f"\nAngulo en grados: {angulo_grados}°")
print(f"Seno: {seno: .4f}")
print(f"Coseno: {coseno: .4f}")
print(f"Tangente: {tangente: .4f}")
