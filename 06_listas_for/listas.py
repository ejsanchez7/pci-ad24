def imprime_datos(datos):
    contador = 0

    while contador < len(datos):
        print(datos[contador])
        contador += 1

def promedio(numeros):
    contador = 0
    suma = 0

    while contador < len(numeros):
        suma += numeros[contador]
        contador += 1
    
    return suma / len(numeros)

def multiplicar_por_dos(lista):
    contador = 0

    while contador < len(lista):
        lista[contador] = lista[contador] * 2
        contador += 1
    
    return lista

def duplica(num) :
    num = num * 2
    #return numero * 2

info = [10, 20, 30, 40]
print(multiplicar_por_dos(info))
print(info)

num = 4
print(duplica(num))
print(num)
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