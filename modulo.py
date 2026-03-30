def temperatura_a_fahrenheit(celsius):
    """Convierte temperatura de Celsius a Fahrenheit.

    Args:
        celsius (float): Temperatura en Celsius.

    Returns:
        float: Temperatura en Fahrenheit.
    """
    return (celsius * 9/5) + 32

def temperatura_a_celsius(fahrenheit):
    """Convierte temperatura de Fahrenheit a Celsius.

    Args:
        fahrenheit (float): Temperatura en Fahrenheit.

    Returns:
        float: Temperatura en Celsius.
    """
    return (fahrenheit - 32) * 5/9