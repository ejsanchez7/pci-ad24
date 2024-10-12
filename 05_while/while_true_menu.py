def menu():
    print("a.- Imprimir mensaje.")
    print("b.- Salir")
    opcion = input("Selecciona una opción: ")

    return opcion.lower()

def imprimir_mensaje():
    print("Saludos!!!")

continuar = True

while continuar:
# while True :
    opcion = menu()

    if opcion == 'a':
        imprimir_mensaje()
    elif opcion == 'b':
        #break
        continuar = False
    else:
        print("Opción no válida")