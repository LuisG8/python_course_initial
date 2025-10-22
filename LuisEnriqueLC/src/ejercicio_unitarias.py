import requests
class Cliente:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
    
    def validar_email(self) -> bool:
        """" Valida la estructura de mi correo"""
        return "@" in self.correo and "." in self.correo
    def __str__(self):
        return 
 
class Httpllamadas:
    def __init__(self, url):
        self.url = url
    def get_data(self, id:int):
        response = requests.get(f"{self.url}/{id}")
        return response.json()

http = Httpllamadas("https://rickandmortyapi.com/api/character")
print(http.get_data(10))
    
#Funcion que descuenta
class Producto:
    def __init__(self, precio: float):
        self.precio = precio
    def aplicar_descuento(self, porcentaje: float) -> float:
        """ Aplica un descuento a un precio de producto"""
        descuento = self.precio * (porcentaje/100)
        return self.precio - descuento



    
client = Cliente ("Luis", "correo")

print(client.validar_email())
