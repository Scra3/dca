import portfolio as portfolio
import price_history as ph
import app as app
import pytest
import dca as algo


@pytest.fixture
def drop_databases_after_test():
    yield
    portfolio.Portfolio().drop_db()
    ph.PriceHistory().drop_db()


class PriceHistoryStub(ph.PriceHistory):
    prices = [200, 300, 250, 150]
    count_call = -1

    @staticmethod
    def get_current_bitcoin_price() -> float:
        PriceHistoryStub.count_call = PriceHistoryStub.count_call + 1
        return PriceHistoryStub.prices[PriceHistoryStub.count_call]


def test_app_run_4_times(drop_databases_after_test):
    app_runner = app.App(price_history=PriceHistoryStub(), dca=algo.Dca(price_initialisation=20, step_price=1))
    
    app_runner.run()
    prices = ph.PriceHistory().get_prices()
    total_spent = portfolio.Portfolio().get_total_spent()

    assert total_spent == 20
    assert prices == [200]

    app_runner.run()

    prices = ph.PriceHistory().get_prices()
    total_spent = portfolio.Portfolio().get_total_spent()

    assert total_spent == 20 + 0
    assert prices == [200, 300]

    app_runner.run()

    prices = ph.PriceHistory().get_prices()
    total_spent = portfolio.Portfolio().get_total_spent()

    assert total_spent == 20 + 0 + 0
    assert prices == [200, 300, 250]

    app_runner.run()

    prices = ph.PriceHistory().get_prices()
    total_spent = portfolio.Portfolio().get_total_spent()

    assert total_spent == 20 + 0 + 0 + (21 + 22 + 23)
    assert prices == [200, 300, 250, 150]
