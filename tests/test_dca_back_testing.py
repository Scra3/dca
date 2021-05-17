import dca_runner as runner
import model
import stub
import data
import typing
import datetime as dt
from fixtures import drop_databases


def get_only_tuesday_prices(prices: typing.List[float]) -> typing.List[float]:
    filtered_prices = []
    for price in prices:
        timestamp = price[0] / 1000
        date = dt.datetime.fromtimestamp(timestamp)
        if date.weekday() == 2:
            filtered_prices.append(price[1])

    return filtered_prices


def test_dca_runner_with_real_btc_prices(drop_databases):
    dca_configuration = model.DcaConfiguration(
        price_initialisation=20,
        step_price=1,
        force_buy_under_price=3600,
        traded_pair=model.PairMapping.XBTUSDC,
    )
    broker = stub.BrokerStub()
    broker.prices = get_only_tuesday_prices(data.btc_prices)

    dca_runner = runner.DcaRunner(broker=broker, dca_configuration=dca_configuration)

    # run dca for each prices
    for _ in range(len(broker.prices)):
        dca_runner.run()

    prices = model.PriceHistory.get_prices()
    total_spent = model.Portfolio.get_total_spent()
    balance = model.Portfolio.get_balance()
    average = model.Portfolio.get_average_price()

    assert len(prices) == len(broker.prices)
    assert total_spent == 2585
    assert balance == 0.6857170924475
    assert average == 3769.7762363972474


def test_dca_runner_with_real_eth_prices(drop_databases):
    dca_configuration = model.DcaConfiguration(
        price_initialisation=20,
        step_price=1,
        traded_pair=model.PairMapping.XBTUSDC,
        force_buy_under_price=150,
        max_total_amount_to_spend=2000,
    )
    broker = stub.BrokerStub()
    broker.prices = get_only_tuesday_prices(data.eth_prices)

    dca_runner = runner.DcaRunner(broker=broker, dca_configuration=dca_configuration)

    # run dca for each prices
    for _ in range(len(broker.prices)):
        dca_runner.run()

    prices = model.PriceHistory.get_prices()
    total_spent = model.Portfolio.get_total_spent()
    balance = model.Portfolio.get_balance()
    average = model.Portfolio.get_average_price()

    assert len(prices) == len(broker.prices)
    assert balance == 12.559736986288318
    assert total_spent == 1898.0
    assert average == 151.1178141765293
