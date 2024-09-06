# Una función que determina, dados 2 valores, cuál es el mayor.
def mayor(num1, num2) :
    if num1 > num2 :
        return num1
    return num2

'''
Una función que calcula la corriente de un circuito conociendo el voltaje y 
la resistencia, suponga que el valor de la resistencia no puede ser negativo.
corriente = voltaje / resistencia
'''
def calcular_corriente(voltaje, resistencia) :
    if resistencia <= 0 :
        print("No se puede calcular la corriente")
    else :
        corriente = voltaje / resistencia
        print(f"La corriente es: {corriente}")

'''
Dadas tres cantidades enteras positivas, se quiere determinar las siguientes situaciones:

¿Es un triángulo? Si los valores de dichas cantidades pueden corresponder a las longitudes de los lados de un triángulo.
¿Es escaleno? En el caso de que las medidas puedan corresponder a las longitudes de los lados de un triángulo, si dicho triángulo es escaleno.
¿Es equilátero? En el caso de que las medidas puedan corresponder a las longitudes de los lados de un triángulo, si dicho triángulo es equilátero.
¿Es isósceles? En el caso de que las medidas puedan corresponder a las longitudes de los lados de un triángulo, si dicho triángulo es isósceles.
'''
def tipo_triangulo(a, b, c) :
    if (a + b) > c and (a + c) > b and (b + c) > a :
        # Es un triángulo
        if a == b and b == c :
            print("Equilátero")
        elif a == b or a == c or b == c:
            print("Isóceles")
        else :
            print("Escaleno")
    else:
        print("No es un triángulo")

'''
Determinar si un año es bisiesto. Un año es bisiesto si es múltiplo de 4 (por ejemplo, 1984). 
Sin embargo, los años múltiplos de 100 sólo son bisiestos cuando a la vez son múltiplos de 
400 (por ejemplo, 1800 no es bisiesto, mientras que 2000 si lo es).
'''
def es_bisiesto(anio) :
    if anio % 4 == 0 :
        if anio % 100 == 0 :
            if anio % 400 == 0 :
                print("Es bisiesto")
        else:
            print("Es bisiesto")


# print(mayor(56, 4))
# print(mayor(1, 2))
# print(mayor(-10, -1))

#print(calcular_corriente(100, 10))

tipo_triangulo(10, 5, 1) # No es un triángulo
tipo_triangulo(7, 7, 7) # Equilátero
tipo_triangulo(14, 8, 14) # Isóseles
tipo_triangulo(5, 9, 12) # Escaleno
