import bcrypt
import jwt
from datetime import datetime, timedelta

class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

def registro(nombre, contrasena):
    return Usuario(nombre, contrasena)

def login(nombre, contrasena):
    usuario = Usuario(nombre, contrasena)
    if bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': nombre
        }
        return jwt.encode(payload, 'secret', algorithm='HS256')
    return None

def protegida(token):
    if token is None:
        raise Exception('Token no proporcionado')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return 'Hola, ' + payload['sub']
    except jwt.ExpiredSignatureError:
        raise Exception('Token expirado')
    except jwt.InvalidTokenError:
        raise Exception('Token invalido')