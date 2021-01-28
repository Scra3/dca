import portfolio as model
import pytest


@pytest.fixture
def drop_databases_after_test():
    yield
    model.Portfolio().drop_db()


def test_get_total_spent_when_adding_on_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(10)

    total_spent = model.Portfolio().get_total_spent()

    assert total_spent == 10


def test_get_total_spent_when_adding_several_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(10)
    model.Portfolio().save_spent(24.5)

    total_spent = model.Portfolio().get_total_spent()

    assert total_spent == 10 + 24.5


def test_get_average_price():
    price = model.Portfolio.get_average_price(total_spent=10, balance=5)
    assert price == 10 / 5


def test_get_balance():
    balance = model.Portfolio.get_balance(prices=[10, 10], amounts_spent=[1, 1])
    assert balance == 0.1 + 0.1


def test_get_total_spent_from_list():
    amount = model.Portfolio.get_total_spent_from_list(amounts_spent=[1, 1])
    assert amount == 1 + 1
