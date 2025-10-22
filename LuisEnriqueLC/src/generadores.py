#yield

def conteo_to_limit(limit: int):
    """ Contea desde cero hasta el limite """
    print("Inicio de funcion tradicional")
    list = []
    for i in range(limit):
        print("En la posicion", i) # preferible usar f-string
        list.append(i)
    print("Finaliza la funcion tradicional")
    return list

def conteo_gen(limit: int):
    """ Conteo desde cero hasta el limite"""
    print("Inicio de funcion generadora")

    for i in range(limit):
        print("En la posicion", i) # preferible usar f-string
        yield i
    print("Finaliza la funcion generadora")

#conteo_to_limit(10)
##conteo_gen(10)
for numero in conteo_to_limit(5):
    print(f"numero num: {numero}")
for numero in conteo_gen(5):
    print(f"numero num: {numero}")



def fib_n(n: int):
    """ Conteo fibonacci con generador"""
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fib_n(10)), "Fibonacci")

import time

print("Time", time.time())
sum([i**2 for i in range(100000)])
print("Time", time.time())