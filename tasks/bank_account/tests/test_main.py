from main import BankAccount

def test_init_balance():
    account = BankAccount(100.0)
    assert account.get_balance() == 100.0

def test_deposit():
    account = BankAccount()
    account.deposit(50.0)
    assert account.get_balance() == 50.0

def test_withdraw():
    account = BankAccount(100.0)
    account.withdraw(50.0)
    assert account.get_balance() == 50.0

def test_get_balance():
    account = BankAccount(100.0)
    assert account.get_balance() == 100.0

def test_deposit_invalid_amount():
    account = BankAccount()
    try:
        account.deposit(-50.0)
        assert False, "Debería haber lanzado una excepción"
    except ValueError as e:
        assert str(e) == "El monto a depositar debe ser mayor que cero"

def test_withdraw_invalid_amount():
    account = BankAccount()
    try:
        account.withdraw(-50.0)
        assert False, "Debería haber lanzado una excepción"
    except ValueError as e:
        assert str(e) == "El monto a retirar debe ser mayor que cero"

def test_withdraw_insufficient_balance():
    account = BankAccount(50.0)
    try:
        account.withdraw(100.0)
        assert False, "Debería haber lanzado una excepción"
    except ValueError as e:
        assert str(e) == "No hay suficiente saldo para retirar"