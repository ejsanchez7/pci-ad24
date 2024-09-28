'''
F1 = 1
F2 = 1
F3 = F1 + F2 = 1 + 1 = 2
F4 = F2 + F3 = 1 + 2 = 3
F5 = F3 + F4 = 2 + 3 = 5
F6 = F4 + F5 = 3 + 5 = 8
F7 = F5 + F6 = 5 + 8 = 13
'''
def fibonacci(n) :

    ante_anterior = 1
    anterior = 1
    contador = 3

    print("F1: 1")

    if n == 2 :
        print("F2: 1")     

    while n >= 3 and contador <= n :
        print(f"F{contador - 1}: {anterior}")

        actual = ante_anterior + anterior
        ante_anterior = anterior
        anterior = actual
        contador += 1

    print(f"F{contador - 1}: {anterior}")
        
fibonacci(2)
print("************************")
fibonacci(3)
print("************************")
fibonacci(4)
print("************************")
fibonacci(5)
print("************************")
fibonacci(6)
print("************************")
fibonacci(7)
