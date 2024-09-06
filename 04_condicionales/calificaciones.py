'''
Pedir al usuario la calificación de los dos parciales (entre 0 y 100)
promediarlos e indicar si aprobó (>=70)
'''
def calcular_promedio(cal1, cal2) :
    return (cal1 + cal2) / 2

def aprueba(cal) :
    return cal >= 70

def valida_calificacion(cal) :
    return cal >= 0 and cal <= 100

calificacion1 = float(input("Escribe la calificación del parcial 1: "))
calificacion2 = float(input("Escribe la calificación del parcial 2: "))

if valida_calificacion(calificacion1) :
    if valida_calificacion(calificacion2) :
        # Promediar y verificar si aprobó
        promedio = calcular_promedio(calificacion1, calificacion2)
        if aprueba(promedio) :
            print("Aprobaste el semestre")
        else:
            print("Nos vemos el siguiente semestre")
    else:
        print("La calificación del parcial 2 es incorrecta")
else:
    print("La calificación del parcial 1 es incorrecta")
