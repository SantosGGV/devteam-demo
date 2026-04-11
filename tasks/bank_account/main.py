class BankAccount:
    """
    Represents a bank account with methods to deposit, withdraw and get the balance.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes a bank account with an optional initial balance.
        """
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.
        Args:
            amount (float): The amount to deposit.
        Returns:
            float: The updated balance.
        Raises:
            ValueError: If the amount is not greater than 0.
        """
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError('Amount must be greater than 0')

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.
        Args:
            amount (float): The amount to withdraw.
        Returns:
            float: The updated balance.
        Raises:
            ValueError: If the amount is not greater than 0 or if there are insufficient funds.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        elif amount <= 0:
            raise ValueError('Amount must be greater than 0')
        else:
            raise ValueError('Insufficient funds')

    def get_balance(self):
        """
        Returns the current balance of the account.
        Returns:
            float: The current balance.
        """
        return self.balance