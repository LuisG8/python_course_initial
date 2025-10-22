# args

#Argumentos posicionales
def procesar_datos(*args) -> None:
    """" Recibe argumentos posicionales """
    print(f"Argumentos: {args}")

#Keyword arguments

def procesar_datos_kw(**kwargs) -> None:
    """" Recibe argumentos posicionales """
    print(f"Argumentos: {kwargs}")

procesar_datos_kw(nombre="Luis", status = True)
procesar_datos(51001,57,-7,-8)