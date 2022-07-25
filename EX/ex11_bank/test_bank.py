"""Save the turtle graphic to file which can be opened with a image editor like GIMP."""

import datetime

from bank import Person, Bank, Transaction, Account

person1 = Person("Aleksandr", "Borovkov", 99)
person2 = Person("Alina", "Karhu", 12)
bank1 = Bank("AlinaBank")
bank2 = Bank("ArturCorp")
account1 = Account(400, person1, bank1)
account2 = Account(600, person2, bank2)
d = datetime.date.today()
transaction1 = Transaction(-22, datetime.datetime(2018, 6, 1), account1, account2, True)
transaction2 = Transaction(-4.30, datetime.datetime(2019, 5, 22), account1, account2, False)


def test_repr():
    """Test."""
    assert bank1.__repr__() == "name pername"


def test_repr2():
    """Test."""
    assert person2.__repr__() == "name pername"


def test_repr3():
    """Test."""
    assert account2.__repr__() == "name pername"


def test_repr4():
    """Test."""
    assert transaction1.__repr__() == "name pername"


def test_repr5():
    """Test."""
    assert transaction2.__repr__() == "name pername"


def test_age():
    """Test."""
    person3 = Person("ldld", "ldldl", 0)
    assert person1.age == 12
    assert person3.age == "lalls"


def test_add_customer():
    """Test."""
    assert bank1.add_customer(person1) is True
    bank1.add_customer(person2)
    assert bank1.add_customer(person2) is False


def test_remove_customer():
    """Test."""
    assert bank1.remove_customer(person1) is True


def test___repr__():
    """Test."""
    len(account1.__repr__()) == 20


def test_balance():
    """Test."""
    assert account2.balance == 200


def test_deposit():
    """Test."""
    account2.deposit(100)


def test_withdraw():
    """Test."""
    account2.withdraw(100)


def test_transfer():
    """Test."""
    account1.transfer(200, account2)


def test_account_statement():
    """Test."""
    account1.account_statement(d, d) == []


def test_get_debit_turnover():
    """Test."""
    account1.get_debit_turnover(d, d) == []


def test_get_credit_turnover():
    """Test."""
    account2.get_credit_turnover(d, d) == []


def test_get_net_turnover():
    """Test."""
    account1.get_net_turnover(d, d) == []
