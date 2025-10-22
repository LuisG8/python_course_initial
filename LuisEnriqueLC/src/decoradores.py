import time


def decorador(func):
    def envoltura(): 
        print("Inicio")
        func()
        print("Final")
    return envoltura

def decorador_tiempo(func):
    def wrapper():
        inicio = time.time()
        func()
        fin = time.time()
        print(f"Tiempo de ejecucion: {fin - inicio} segundos.")
    return wrapper

@decorador
@decorador_tiempo
def saludo():
    #print("Ïnicio")
    print("Hola Mundo")
    time.sleep(20)
    #print("Final")

saludo()


#Generar decorador que calcule el tiempo de ejecucion de una funcion

