import dca_runner as runner
import model
import dataclasses
from fixtures import drop_databases_after_test


@dataclasses.dataclass()
class BrokerStub(model.Broker):
    prices = []
    get_current_pair_price_count_call = 0
    send_buy_order_count_call = 0

    def get_current_pair_price(self, pair: str) -> float:
        self.get_current_pair_price_count_call += 1
        return self.prices[self.get_current_pair_price_count_call - 1]

    def send_buy_order(self, traded_pair: str, amount_to_spend: float, price: float):
        self.send_buy_order_count_call += 1


def test_dca_runner_does_not_call_buy_method_when_amount_spent_is_0(
    drop_databases_after_test,
):
    broker = BrokerStub()
    broker.prices = [200, 300]

    dca_configuration = model.DcaConfiguration(
        price_initialisation=20, step_price=1, traded_pair="XBTEUR"
    )
    dca_runner = runner.DcaRunner(
        broker=broker, dca_configuration=dca_configuration
    )
    # initialisation
    dca_runner.run()

    dca_runner.run()

    assert broker.send_buy_order_count_call == 1


def test_dca_runner_calls_buy_method_when_amount_spent_is_bigger_than_0(
    drop_databases_after_test,
):
    broker = BrokerStub()
    broker.prices = [200, 100]

    dca_configuration = model.DcaConfiguration(
        price_initialisation=20, step_price=1, traded_pair="XBTEUR"
    )
    dca_runner = runner.DcaRunner(
        broker=broker, dca_configuration=dca_configuration
    )
    # initialisation
    dca_runner.run()

    dca_runner.run()

    assert broker.send_buy_order_count_call == 2


def test_dca_runner_4_times(drop_databases_after_test):
    broker = BrokerStub()
    broker.prices = [200, 300, 250, 150]

    dca_configuration = model.DcaConfiguration(
        price_initialisation=20, step_price=1, traded_pair="XBTEUR"
    )
    dca_runner = runner.DcaRunner(
        broker=broker, dca_configuration=dca_configuration
    )

    dca_runner.run()
    prices = model.PriceHistory().get_prices()
    amounts_spent = model.Order().get_amounts_spent()

    assert amounts_spent == [20]
    assert prices == [200]

    dca_runner.run()

    prices = model.PriceHistory().get_prices()
    total_spent = model.Order().get_amounts_spent()

    assert total_spent == [20]
    assert prices == [200, 300]

    dca_runner.run()

    prices = model.PriceHistory().get_prices()
    total_spent = model.Order().get_amounts_spent()

    assert total_spent == [20]
    assert prices == [200, 300, 250]

    dca_runner.run()

    prices = model.PriceHistory().get_prices()
    total_spent = model.Order().get_amounts_spent()

    assert total_spent == [20, 21 + 22 + 23]
    assert prices == [200, 300, 250, 150]
