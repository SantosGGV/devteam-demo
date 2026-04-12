from flask import Flask, request, jsonify
from sqlite3 import connect

app = Flask(__name__)

@app.route('/menu', methods=['GET'])
def obtener_menu():
    """Obtiene la carta del menú.

    :return: La carta del menú como JSON.
    """
    # Código para obtener la carta del menú
    pass

@app.route('/reservas', methods=['POST'])
def crear_reserva():
    """Crea una reserva.

    :param request: El cuerpo de la solicitud con los datos de la reserva.
    :return: El ID de la reserva creada.
    """
    # Código para crear una reserva
    pass

if __name__ == '__main__':
    app.run(debug=True)
