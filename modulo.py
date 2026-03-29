def factorial(n):
    """Calcula el factorial de un numero `n`.

    Args:
        n (int): El numero para calcular el factorial.

    Returns:
        int: El factorial del numero `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Ejemplo de uso
print(factorial(5))