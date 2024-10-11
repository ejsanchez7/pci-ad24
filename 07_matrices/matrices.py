def crea_matriz(default, renglones, columnas):
    matriz = []
    for renglon in range(renglones):
        matriz.append([default] * columnas)
    
    return matriz

def imprime_matriz(matriz):
    # for renglon in range(len(matriz)): #len(matriz) = 7 (número de renglones)
    #    # renglon = 0
    #     for columna in range(len(matriz[renglon])): # len(matriz[renglon]) = 4 (número de columnas)
    #        #columna = 0
    #        print(matriz[renglon][columna], end = ", ")
    #     print("")
    for renglon in matriz:
        # renglon = [5, 5, 5, 5]
        for elemento in renglon:
            print(elemento, end=" ")
        print("")

def matriz_digitos():
    contador = 1
    matriz = []
    for i in range(3):
        lista = []
        for j in range(3):
           lista.append(contador)
           contador += 1
        matriz.append(lista)
    return matriz


matriz = crea_matriz(5, 7, 4)
matriz_irregular = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]
imprime_matriz(matriz_digitos())
