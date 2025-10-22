from abc import ABC, abstractmethod
from dependency_injector import containers, providers

class IRepositorioBD(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass

class RepositorioBD(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Guardando el pedido {pedido} en la base de datos.")

class RepositorioMongoDB(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Guardando el pedido {pedido} en MongoDB.")

class ServicePedido:
    def __init__(self, repositorio: IRepositorioBD):
        self.repositorio = repositorio

    def crear_pedido(self, pedido):
        print(f"Creando el pedido {pedido}.")
        self.repositorio.guardar(pedido)

class Contenedor(containers.DeclarativeContainer):
    repositorio_bd = providers.Singleton(RepositorioBD)
    repositorio_mongo = providers.Singleton(RepositorioMongoDB)
    service_pedido = providers.Factory(
        ServicePedido,
        repositorio=repositorio_bd
    )

container = Contenedor()
service = container.service_pedido()
service.crear_pedido("Pedido #1234")