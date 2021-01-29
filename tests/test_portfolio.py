import pytest
import model


@pytest.fixture
def drop_databases_after_test():
    yield
    model.Portfolio().drop_db()
    model.PriceHistory().drop_db()


def test_get_total_spent_when_adding_on_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(10)

    total_spent = model.Portfolio().get_total_spent()

    assert total_spent == 10


def test_get_total_spent_when_adding_several_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(10)
    model.Portfolio().save_spent(24.5)

    total_spent = model.Portfolio().get_total_spent()

    assert total_spent == 10 + 24.5


def test_get_average_price(drop_databases_after_test):
    model.PriceHistory().save_price(10)
    model.Portfolio().save_spent(20)

    price = model.Portfolio().get_average_price()
    assert price == 10


def test_get_balance(drop_databases_after_test):
    model.PriceHistory().save_price(10)
    model.PriceHistory().save_price(10)
    model.Portfolio().save_spent(1)
    model.Portfolio().save_spent(1)

    balance = model.Portfolio().get_balance()
    assert balance == 0.1 + 0.1
