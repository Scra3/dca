import model
from fixtures import drop_databases_after_test


def test_get_average_price(drop_databases_after_test):
    model.Order(amount=10, price=10).save()

    price = model.Portfolio().get_average_price()

    assert price == 10


def test_get_balance(drop_databases_after_test):
    model.Order(amount=1, price=10).save()
    model.Order(amount=1, price=10).save()

    balance = model.Portfolio().get_balance()

    assert balance == 0.1 + 0.1
