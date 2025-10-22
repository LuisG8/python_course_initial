print("Hola Mundo")
# Comentario en una linea

"""
Comentario multilinea
"""
variable_numero = 3
print(type(variable_numero))

variable_numero = "Soy un string"
print(type(variable_numero))

a, b, c = 1, 2, 3
print (a + b)

a = b = c = 2
print(a*a)

#Comprensiones
#Lista de numeros

numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)
print(type(pares))
