def convertir_temperatura(grados, unidad):
    """
    Convierte temperatura de Celsius a Fahrenheit y viceversa.

    Args:
        grados (float): Temperatura en grados.
        unidad (str): Unidad de medida ('C' o 'F').

    Returns:
        tuple: Temperatura convertida y unidad de medida.
    """
    if unidad == 'C':
        return (grados * 9/5) + 32, 'F'
    elif unidad == 'F':
        return (grados - 32) * 5/9, 'C'