import portfolio as portfolio
import price_history as ph
import app as app
import pytest
import dca as algo
import datetime as dt
import data as data
import typing


@pytest.fixture
def drop_databases_after_test():
    yield
    portfolio.Portfolio().drop_db()
    ph.PriceHistory().drop_db()


def get_only_tuesday_days(prices: typing.List[float]):
    filtered_prices = []
    for price in prices:
        timestamp = price[0] / 1000
        date = dt.datetime.fromtimestamp(timestamp)
        if date.weekday() == 2:
            filtered_prices.append(price)

    return filtered_prices


def test_app_run_4_times(drop_databases_after_test):
    class PriceHistoryStub(ph.PriceHistory):
        prices = [200, 300, 250, 150]
        count_call = -1

        @staticmethod
        def get_current_bitcoin_price() -> float:
            PriceHistoryStub.count_call = PriceHistoryStub.count_call + 1
            return PriceHistoryStub.prices[PriceHistoryStub.count_call]

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


def test_app_run_with_real_prices(drop_databases_after_test):
    class PriceHistoryStub(ph.PriceHistory):
        prices = [price[1] for price in get_only_tuesday_days(data.prices)]
        count_call = -1

        @staticmethod
        def get_current_bitcoin_price() -> float:
            PriceHistoryStub.count_call = PriceHistoryStub.count_call + 1
            return PriceHistoryStub.prices[PriceHistoryStub.count_call]

    app_runner = app.App(price_history=PriceHistoryStub(),
                         dca=algo.Dca(price_initialisation=20, step_price=1, force_buy_under_price=3600))
    for _ in range(55):
        app_runner.run()

    prices = ph.PriceHistory().get_prices()
    total_spent = portfolio.Portfolio().get_total_spent()
    amounts_spent = portfolio.Portfolio().get_amounts_spent()
    balance = portfolio.Portfolio().get_balance(prices=prices, amounts_spent=amounts_spent)
    average = portfolio.Portfolio.get_average_price(balance=balance, total_spent=total_spent)

    assert len(prices) == 55
    assert total_spent == 2585
    assert balance == 0.6857170924475
    assert average == 3769.7762363972474


def test_app_run_with_real_eth_prices(drop_databases_after_test):
    class PriceHistoryStub(ph.PriceHistory):
        prices = [price[1] for price in get_only_tuesday_days(data.eth_prices)]
        count_call = -1

        @staticmethod
        def get_current_bitcoin_price() -> float:
            PriceHistoryStub.count_call = PriceHistoryStub.count_call + 1
            return PriceHistoryStub.prices[PriceHistoryStub.count_call]

    app_runner = app.App(price_history=PriceHistoryStub(),
                         dca=algo.Dca(price_initialisation=20, step_price=1, force_buy_under_price=150,
                                      max_total_amount_to_spend=2000))

    for _ in range(52):
        app_runner.run()

    prices = ph.PriceHistory().get_prices()
    total_spent = portfolio.Portfolio().get_total_spent()
    amounts_spent = portfolio.Portfolio().get_amounts_spent()
    balance = portfolio.Portfolio().get_balance(prices=prices, amounts_spent=amounts_spent)
    average = portfolio.Portfolio.get_average_price(balance=balance, total_spent=total_spent)

    assert len(prices) == 52
    assert balance == 12.559736986288318
    assert total_spent == 1898.0
    assert average == 151.1178141765293
