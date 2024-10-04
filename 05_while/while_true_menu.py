def menu():
    print("1.- Imprimir mensaje.")
    print("2.- Salir")
    opcion = int(input("Selecciona una opción: "))

    return opcion

def imprimir_mensaje():
    print("Saludos!!!")

continuar = True

while continuar:
# while True :
    opcion = menu()

    if opcion == 1:
        imprimir_mensaje()
    elif opcion == 2:
        #break
        continuar = False
    else:
        print("Opción no válida")