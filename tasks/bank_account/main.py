class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero")
        if amount > self.balance:
            raise ValueError("No hay suficiente saldo para retirar")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance