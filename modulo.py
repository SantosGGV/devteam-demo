class Stack:
    def __init__(self) -> None:
        self._elements: list[int] = []

    def push(self, value: int) -> None:
        self._elements.append(value)

    def pop(self) -> int:
        if not self._elements:
            raise IndexError('Pila vacía')
        return self._elements.pop()

    def peek(self) -> int:
        if not self._elements:
            raise IndexError('Pila vacía')
        return self._elements[-1]
