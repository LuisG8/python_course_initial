#Funcion
def saludar(nombre: str) -> str:
    '''Funcion que devuelve un saludo'''
    return f"Hola {nombre}"

print(saludar("Luis"))

#Funcion con argumento por default
def saludo_generico(nombre = "Usuario") -> str:
    return f"Hola {nombre}"

print(saludo_generico())

#Funcion con argumento kwargs

#Lambda

def suma(num1: int, num2: int) -> int:
    """"Suma de 2 numeros"""
    return num1 + num2


suma_lambda = lambda n1, n2: n1+n2

print(suma(2,3))
print(suma_lambda(2,3))

#Map y filter
#Map
lista_numeros = [1,2,3,4,5]
tipo_dato = type(map(lambda x: x**2, lista_numeros))
print(tipo_dato)
cuadrados = list(map(lambda x: x**2, lista_numeros))

print(cuadrados)

#Filter

pares = list(filter(lambda n: n%2 ==0, lista_numeros))
print(pares)
print(type(pares))