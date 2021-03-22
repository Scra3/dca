import pytest
import model


@pytest.fixture
def drop_databases_after_test():
    yield
    model.Portfolio().drop_db()
    model.PriceHistory().drop_db()


def test_get_total_spent_when_adding_on_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(amount=10, price=10)

    total_spent = model.Portfolio().get_total_spent()

    assert total_spent == 10


def test_get_total_spent_when_adding_several_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(amount=10, price=10)
    model.Portfolio().save_spent(amount=24.5, price=10)

    total_spent = model.Portfolio().get_total_spent()

    assert total_spent == 10 + 24.5


def test_get_average_price(drop_databases_after_test):
    model.Portfolio().save_spent(amount=10, price=10)

    price = model.Portfolio().get_average_price()
    assert price == 10


def test_get_balance(drop_databases_after_test):
    model.Portfolio().save_spent(amount=1, price=10)
    model.Portfolio().save_spent(amount=1, price=10)

    balance = model.Portfolio().get_balance()

    assert balance == 0.1 + 0.1
