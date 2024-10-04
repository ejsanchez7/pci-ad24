
def imprime_datos(datos):
    for elemento in datos:
        print(elemento, end=", ")
    print("")

def promedio(numeros):
    suma = 0

    for i in range(0, len(numeros)):
        suma += numeros[i]
    
    return suma / len(numeros)

def multiplicar_por_dos(lista):
    
    salida = lista.copy()

    for i in range(0, len(salida)):
        salida[i] = salida[i] * 2
    
    return salida

def genera_lista(limite):
    lista = []

    for i in range(0, limite):
        numero = int(input("Escribe un número: "))
        #lista.insert(i, numero)
        lista.append(numero)
    
    return lista

info = genera_lista(3)
info.insert(1, 10)
print(multiplicar_por_dos(info))
imprime_datos(info)
print(promedio(info))
# print(info[2])
# print(len(info))
# print(info)
# print(promedio(info))
# print("-------------------")
# imprime_datos(info)

# 10
# 20
# 30
# 40