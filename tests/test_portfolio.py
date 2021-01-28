import portfolio as portfolio
import pytest
import price_history as price_history


@pytest.fixture
def drop_databases_after_test():
    yield
    portfolio.Portfolio().drop_db()
    price_history.PriceHistory().drop_db()


def test_get_total_spent_when_adding_on_amount_spent(drop_databases_after_test):
    portfolio.Portfolio().save_spent(10)

    total_spent = portfolio.Portfolio().get_total_spent()

    assert total_spent == 10


def test_get_total_spent_when_adding_several_amount_spent(drop_databases_after_test):
    portfolio.Portfolio().save_spent(10)
    portfolio.Portfolio().save_spent(24.5)

    total_spent = portfolio.Portfolio().get_total_spent()

    assert total_spent == 10 + 24.5


def test_get_average_price(drop_databases_after_test):
    price_history.PriceHistory().save_price(10)
    portfolio.Portfolio().save_spent(20)

    price = portfolio.Portfolio().get_average_price()
    assert price == 10


def test_get_balance(drop_databases_after_test):
    price_history.PriceHistory().save_price(10)
    price_history.PriceHistory().save_price(10)
    portfolio.Portfolio().save_spent(1)
    portfolio.Portfolio().save_spent(1)

    balance = portfolio.Portfolio().get_balance()
    assert balance == 0.1 + 0.1
