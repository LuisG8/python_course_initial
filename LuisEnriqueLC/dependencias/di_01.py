"""
Inyeccion por constructor
"""
""" 
#Clase que almacena el pedido
class RepositorioBD:

    def save(self, pedido: str):
        print("Pedido {pedido} almacenado exitosamente")
#Clase que implementa logica de negocio del pedido
class ServicePedidos:
    def __init__(self, repositorio: RepositorioBD):
        self.repositorio = repositorio

    def crear_pedido(self, pedido: str):
            print("Notificacion por mensaje")
            print("Impresion de orden")
            self.repositorio.save(pedido)
            print("Notificaicon de almacenado")

repo = RepositorioBD()
service = ServicePedidos(repo)

service.crear_pedido("Hamburguesita")
 """

"""" Setter Inyeccion """


#Clase que almacena el pedido
""" class RepositorioBD:

    def save(self, pedido: str):
        print("Pedido {pedido} almacenado exitosamente")
#Clase que implementa logica de negocio del pedido
class ServicePedidos:
    def set_repo(self, repositorio: RepositorioBD):
        #Inicializa la instancia de mi repositorio
        self.repositorio = repositorio

    def crear_pedido(self, pedido: str):
            print("Notificacion por mensaje")
            print("Impresion de orden")
            self.repositorio.save(pedido)
            print("Notificaicon de almacenado")

repo = RepositorioBD()
service = ServicePedidos()

service.set_repo(repo)

service.crear_pedido("Hamburguesita")
 """

""" from abc import ABC, abstractmethod

class IRepositorioDB(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass

class RepositorioDB(IRepositorioDB):
    def guardar(self, pedido):
        print("Pedido {pedido} almacenado exitosamente")

class ServicePedido:
    def __initi__(self, repositorio: IRepositorioDB):
        self.repositorio = repositorio
    def crear_pedido(self, pedido: str):
            print("Notificacion por mensaje")
            print("Impresion de orden")
            self.repositorio.save(pedido)
            print("Notificaicon de almacenado")

repoDB: IRepositorioDB = RepositorioDB()
service = ServicePedido(Repositorio = repoDB)

service.crear_pedido("tacos") """


""" Inyeccion manual de dependencias"""

from abc import abstractmethod


class IRepositorioBD(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass

class RepositorioBD(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Guardando el pedido {pedido} en la base de datos.")

class ServicePedido:
    def __init__(self, repositorio: IRepositorioBD):
        self.repositorio = repositorio

    def crear_pedido(self, pedido):
        print(f"Creando el pedido {pedido}.")
        self.repositorio.guardar(pedido)

class Container:
    def __init__(self):
        self._services = {}

    def register(self, name, service):
        self._services[name] = service

    def resolve(self, name):
        service = self._services.get(name)
        if not service:
            raise ValueError(f"Service '{name}' not found in container.")
        return service

container = Container()
container.register("repositorio", lambda: RepositorioBD())
container.register("service_pedido", lambda: ServicePedido(container.resolve("repositorio")()))

service = container.resolve("service_pedido")()
service.crear_pedido("Pedido #1234")