def convertir_temperatura(temperatura, unidad_inicial, unidad_final):
    # Código para convertir temperaturas

    if unidad_inicial == 'Celsius' and unidad_final == 'Fahrenheit':
        return (temperatura * 9/5) + 32
    elif unidad_inicial == 'Fahrenheit' and unidad_final == 'Celsius':
        return (temperatura - 32) * 5/9
    elif unidad_inicial == 'Kelvin' and unidad_final == 'Celsius':
        return temperatura - 273.15
    elif unidad_inicial == 'Celsius' and unidad_final == 'Kelvin':
        return temperatura + 273.15
    elif unidad_inicial == 'Fahrenheit' and unidad_final == 'Kelvin':
        return (temperatura - 32) * 5/9 + 273.15
    elif unidad_inicial == 'Kelvin' and unidad_final == 'Fahrenheit':
        return (temperatura - 273.15) * 9/5 + 32
    else:
        return None

    # Docstrings para la función
    """
    Convierte una temperatura de una unidad a otra.

    Parámetros
    ----------
    temperatura : float
        La temperatura a convertir.
    unidad_inicial : str
        La unidad de la temperatura inicial (Celsius, Fahrenheit o Kelvin).
    unidad_final : str
        La unidad de la temperatura final (Celsius, Fahrenheit o Kelvin).

    Retorna
    -------
    float
        La temperatura convertida.
    """