import model
from fixtures import drop_databases_after_test


def test_get_total_spent_when_adding_on_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(amount=10, price=10, time=10.0)

    total_spent = model.Portfolio().get_total_spent()

    assert total_spent == 10


def test_get_total_spent_when_adding_several_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(amount=10, price=10, time=10.0)
    model.Portfolio().save_spent(amount=24.5, price=10, time=10.0)

    total_spent = model.Portfolio().get_total_spent()

    assert total_spent == 10 + 24.5


def test_get_average_price(drop_databases_after_test):
    model.Portfolio().save_spent(amount=10, price=10, time=10.0)

    price = model.Portfolio().get_average_price()
    assert price == 10


def test_get_balance(drop_databases_after_test):
    model.Portfolio().save_spent(amount=1, price=10, time=10.0)
    model.Portfolio().save_spent(amount=1, price=10, time=10.0)

    balance = model.Portfolio().get_balance()

    assert balance == 0.1 + 0.1
