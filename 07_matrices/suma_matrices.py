def crea_matriz(default, renglones, columnas):
    matriz = []
    for renglon in range(renglones):
        matriz.append([default] * columnas)
    
    return matriz

def imprime_matriz(matriz):
    for renglon in matriz:
        for elemento in renglon:
            print(elemento, end=" ")
        print("")

def suma_matrices(matriz1, matriz2):
    # validar que sean del mismo tamaño
    if (len(matriz1) == len(matriz2)) and (len(matriz1[0]) == len(matriz2[0])):
        num_renglones = len(matriz1)
        num_columnas = len(matriz1[0])
        # resultado = [[0] * len(matriz1[0])] * len(matriz1)
        resultado = crea_matriz(0, num_renglones, num_columnas)

        for i in range(num_renglones):
            for j in range(num_columnas):
                resultado[i][j] = matriz1[i][j] + matriz2[i][j]

        return resultado

m1 = [
        [1, 2],
        [3, 4]
    ]
m2 = [
        [5, 6],
        [7, 8]
    ]

print(suma_matrices(m1, m2))