from math import pi

# Volumen de un cilindro
print(f"PI = {pi}")
radio = float(input("Escribe el radio: "))
altura = float(input("Escribe la altura: "))
volumen = pi * radio ** 2 * altura / 2

print(f"El volumen de un círculo de radio {radio} y altura {altura} = {volumen}")