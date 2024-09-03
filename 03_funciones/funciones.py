from math import pi

# Volumen de un cilindro

# Definición/declaración de la función
def calcular_volumen_cilindro(radio, altura) :  
    volumen = pi * radio ** 2 * altura / 2
    return volumen

# Convertir grados farenheit a Celsius (Celsius = 5 / 9 ( Farenheit – 32))
def farenheit2celsius(grados_f) :
    return 5 / 9 * (farenheit - 32)

#Convertir millas a kilómetros
def millas2kilometros(cant_millas) :
    cant_km = cant_millas * 1.609
    return cant_km

# Mandar llamar farenheit2celsius
# farenheit = float(input("Escribe los grados Farenheit: "))
# print(f"{farenheit} grados Farenheit son {farenheit2celsius(farenheit)} grados Celsius")

millas = float(input("Escribe el número de millas: "))
kilometros = millas2kilometros(millas)
print(f"{millas} millas = {kilometros}km")

# Mandar llamar la función
# rad = float(input("Escribe el radio: "))
# alt = float(input("Escribe la altura: "))
# vol = calcular_volumen_cilindro(rad, alt)
# #vol2 = calcular_volumen_cilindro(5, 6)
# print(f"El volumen de un círculo de radio {rad} y altura {alt} = {vol}")