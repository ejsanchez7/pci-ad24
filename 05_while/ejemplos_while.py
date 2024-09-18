import math

# Sumatoria de los números enteros desde 1 hasta n
def sumatoria(n):
    resultado = 0
    contador = 1

    while contador <= n:
        resultado = resultado + contador
        contador = contador + 1

    return resultado

def sumatoria2(n):
    resultado = 0

    while n >= 1:
        resultado = resultado + n
        n = n - 1

    return resultado

# Encuentra los pares menores a "numero"
def pares(numero):
    contador = 1

    while contador < numero:
        if contador % 2 == 0:
            print(contador)
        contador = contador + 1

def pares_mejorada(numero):
    contador = 2

    while contador < numero:
        print(contador, end = ",")
        contador = contador + 2 # contador += 2
    print("")

# cuenta los pares menores a "numero"
def cuenta_pares(numero):
    contador = 1
    resultado = 0

    while contador < numero:
        if contador % 2 == 0:
            resultado = resultado + 1
        contador = contador + 1
    
    return resultado

def f_while(n):
    resultado=0
    i=1
    while i<= n:
        term=(i**2-3*i)/ math.sqrt(5*i)
        resultado+= term
        i+= 1
    return resultado

def promedio():
    continuar = "s"
    total = 0
    contador = 0

    while True:
        total = total + float(input("Escribe el número: "))
        contador += 1
        continuar = input("¿Deseas continuar (s/n)? ")
        if continuar == "n":
            break

    return (total / contador)

def promedio2():
    continuar = "s"
    total = 0
    contador = 0

    while continuar != "n":
        total = total + float(input("Escribe el número: "))
        contador += 1
        continuar = input("¿Deseas continuar (s/n)? ")

    return (total / contador)

print(f"El promedio es: {promedio2()}")

#n=5
#print (f_while(n))

#print(sumatoria(5))
#print(sumatoria2(5))
#pares_mejorada(20)
#print("------------------")
#print(cuenta_pares(20))