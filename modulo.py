def factorial(n):
    """Calcula el factorial de un numero.

    Args:
        n (int): El numero para calcular el factorial.

    Returns:
        int: El factorial del numero.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Ejemplo de uso
print(factorial(5))