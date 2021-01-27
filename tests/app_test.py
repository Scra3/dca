import portfolio as portfolio
import price_history as ph
import app as app
import pytest


@pytest.fixture
def drop_databases_after_test():
    yield
    portfolio.Portfolio.drop_db()
    ph.PriceHistory.drop_db()


def test_app(drop_databases_after_test):
    app.App.run()

    prices = ph.PriceHistory.get_prices()
    total_spent = portfolio.Portfolio.get_total_spend()

    assert total_spent > 0
    assert len(prices) == 1
