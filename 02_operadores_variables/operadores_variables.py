'''
Tipos de datos:
    - Números: enteros y floats (decimales)
    - Cadenas de texto: strings
    - booleanos: True/False
'''

'''
Operadores:
    Nivel 1
        ** (potencia): elevar un número a un exponente
    Nivel 2
        % (módulo): residuo de una división entera
        // (división entera): resultado de una división sin los decimales
        * (multiplicación)
        / (división)
    Nivel 3
        + (suma)
        - (resta)
'''

cateto_a = 5 # Entero
cateto_b = 4.0 # Flotante

# Operador de potencia **
hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5

#Imprimir un valor
print(f"La hipotenusa de {cateto_a} y {cateto_b} es: {hipotenusa}")

# Calcular el área de un círculo
PI = 3.1416 # Float
radio = float(input("Escribe el radio: "))
# radio = float(radio)
area = PI * radio ** 2
perimetro = PI * radio * 2

print(f"El área de un círculo de radio {radio} es: {area:.2f}")
print(f"El perímetro de un círculo de radio {radio} es: {perimetro:.2f}")
