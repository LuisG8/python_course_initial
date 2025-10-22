from unittest.mock import Mock
from src.ejercicio_unitarias import Cliente
from src.ejercicio_unitarias import Httpllamadas
def test_validar_email_success():
    #Arrange
    email_valido = "email@tet.com"
    #Llamada
    cliente_test = Cliente("Luis", email_valido)
    #Assert
    assert cliente_test.validar_email() is True

def test_make_request_success(monkeypatch):
    #arrange
    id = 20
    http_mock = Mock(status_code = 200)
    http_mock.json.return_value = {'some':'data'}
    monkeypatch.setattr("requests.get", lambda url: http_mock)

    http_client = Httpllamadas("http://localhost:80/url/example.com")
    response = http_client.get_data(id)

    assert response is not None