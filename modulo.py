class Stack:
    """Clase que implementa una pila con métodos push, pop y peek."""

    def __init__(self):
        """Inicializa la pila vacía."""
        self.elementos = []

    def push(self, elemento):
        """Agrega un elemento a la pila."""
        self.elementos.append(elemento)

    def pop(self):
        """Elimina y devuelve el último elemento de la pila. Si la pila está vacía, levanta una excepción IndexError."""
        if self.elementos:
            return self.elementos.pop()
        else:
            raise IndexError('Pila vacía')

    def peek(self):
        """Devuelve el último elemento de la pila sin eliminarlo. Si la pila está vacía, levanta una excepción IndexError."""
        if self.elementos:
            return self.elementos[-1]
        else:
            raise IndexError('Pila vacía')