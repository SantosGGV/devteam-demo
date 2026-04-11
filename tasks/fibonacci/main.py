def fibonacci(n):
    """Calcula el número de Fibonacci para n.

    Args:
        n (int): El número para el que se calcula el número de Fibonacci.

    Returns:
        int: El número de Fibonacci para n.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)