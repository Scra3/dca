import portfolio as portfolio
import price_history as ph
import app as app
import pytest


@pytest.fixture
def drop_databases_after_test():
    yield
    portfolio.Portfolio().drop_db()
    ph.PriceHistory().drop_db()


class PriceHistoryStub(ph.PriceHistory):
    @staticmethod
    def get_current_bitcoin_price() -> float:
        return 200


def test_app_run_5_times(drop_databases_after_test):
    for _ in range(5):
        app.App(price_history=PriceHistoryStub()).run()

    prices = ph.PriceHistory().get_prices()
    total_spent = portfolio.Portfolio().get_total_spent()

    assert total_spent == 20 + 21 + 22 + 23 + 24
    assert len(prices) == 5
