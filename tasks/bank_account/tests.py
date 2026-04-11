import unittest
from tasks.bank_account.main import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount()
        self.assertEqual(account.deposit(100), 100)

    def test_withdraw(self):
        account = BankAccount(initial_balance=100)
        self.assertEqual(account.withdraw(50), 50)

    def test_insufficient_funds(self):
        account = BankAccount(initial_balance=100)
        with self.assertRaises(ValueError):
            account.withdraw(150)

    def test_invalid_amount(self):
        account = BankAccount()
        with self.assertRaises(ValueError):
            account.deposit(-100)

if __name__ == '__main__':
    unittest.main()