import pytest
from modulo import Usuario, login, registro, protegida
from pytest import raises
import bcrypt
import jwt

@pytest.fixture
def usuario():
    return Usuario('usuario', 'contrasena')

def test_registro():
    usuario = registro('usuario', 'contrasena')
    assert usuario.nombre == 'usuario'
    assert bcrypt.checkpw(b'contrasena', usuario.contrasena)

def test_login():
    registro('usuario', 'contrasena')
    token = login('usuario', 'contrasena')
    assert token is not None

def test_protegida():
    registro('usuario', 'contrasena')
    token = login('usuario', 'contrasena')
    assert protegida(token) == 'Hola, usuario'

def test_protegida_sin_token():
    with raises(Exception):
        protegida(None)
