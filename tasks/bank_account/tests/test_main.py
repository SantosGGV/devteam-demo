from main import BankAccount

def test_bank_account_initial_balance():
    account = BankAccount()
    assert account.get_balance() == 0.0

def test_bank_account_deposit():
    account = BankAccount()
    account.deposit(100.0)
    assert account.get_balance() == 100.0

def test_bank_account_withdraw():
    account = BankAccount(100.0)
    account.withdraw(50.0)
    assert account.get_balance() == 50.0

def test_bank_account_get_balance():
    account = BankAccount(100.0)
    assert account.get_balance() == 100.0

def test_bank_account_deposit_invalid_amount():
    account = BankAccount()
    try:
        account.deposit(-10.0)
        assert False, "Se esperaba una excepción ValueError"
    except ValueError as e:
        assert str(e) == "El monto a depositar debe ser mayor que cero"

def test_bank_account_withdraw_invalid_amount():
    account = BankAccount()
    try:
        account.withdraw(-10.0)
        assert False, "Se esperaba una excepción ValueError"
    except ValueError as e:
        assert str(e) == "El monto a retirar debe ser mayor que cero"

def test_bank_account_withdraw_insufficient_balance():
    account = BankAccount(10.0)
    try:
        account.withdraw(20.0)
        assert False, "Se esperaba una excepción ValueError"
    except ValueError as e:
        assert str(e) == "No hay suficiente saldo para realizar la transacción"