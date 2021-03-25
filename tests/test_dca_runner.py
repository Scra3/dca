import dca_runner as runner
import pytest
import model


@pytest.fixture
def drop_databases_after_test():
    yield
    model.Portfolio().drop_db()
    model.PriceHistory().drop_db()


def test_dca_runner_does_not_call_buy_method_when_amount_spent_is_0(drop_databases_after_test):
    class BrokerStub(model.Broker):
        prices = [200, 300]
        get_current_pair_price_count_call = -1
        send_buy_order_count_call = 0

        @staticmethod
        def get_current_pair_price(pair: str) -> float:
            count_call = BrokerStub.get_current_pair_price_count_call + 1
            BrokerStub.get_current_pair_price_count_call = count_call
            return BrokerStub.prices[count_call]

        def send_buy_order(self, traded_pair: str, amount_to_spent: float, price: float):
            count_call = BrokerStub.send_buy_order_count_call
            BrokerStub.send_buy_order_count_call = count_call + 1
            pass

    broker_stub = BrokerStub()
    dca_configuration = model.DcaConfiguration(price_initialisation=20, step_price=1,
                                               traded_pair="XBTEUR")

    dca_runner = runner.DcaRunner(broker=broker_stub,
                                  dca_configuration=dca_configuration)
    # initialisation
    dca_runner.run()

    dca_runner.run()

    assert broker_stub.send_buy_order_count_call == 1


def test_dca_runner_calls_buy_method_when_amount_spent_is_bigger_than_0(drop_databases_after_test):
    class BrokerStub(model.Broker):
        prices = [200, 100]
        get_current_pair_price_count_call = -1
        send_buy_order_count_call = 0

        @staticmethod
        def get_current_pair_price(pair: str) -> float:
            count_call = BrokerStub.get_current_pair_price_count_call + 1
            BrokerStub.get_current_pair_price_count_call = count_call
            return BrokerStub.prices[count_call]

        def send_buy_order(self, traded_pair: str, amount_to_spent: float, price: float):
            count_call = BrokerStub.send_buy_order_count_call
            BrokerStub.send_buy_order_count_call = count_call + 1
            pass

    dca_configuration = model.DcaConfiguration(price_initialisation=20, step_price=1,
                                               traded_pair="XBTEUR")
    dca_runner = runner.DcaRunner(broker=BrokerStub(),
                                  dca_configuration=dca_configuration)
    # initialisation
    dca_runner.run()

    dca_runner.run()

    assert BrokerStub.send_buy_order_count_call == 2


def test_dca_runner_4_times(drop_databases_after_test):
    class BrokerStub(model.Broker):
        prices = [200, 300, 250, 150]
        count_call = -1

        @staticmethod
        def get_current_pair_price(pair: str) -> float:
            BrokerStub.count_call = BrokerStub.count_call + 1
            return BrokerStub.prices[BrokerStub.count_call]

        def send_buy_order(self, traded_pair: str, amount_to_spent: float, price: float):
            pass

    dca_configuration = model.DcaConfiguration(price_initialisation=20, step_price=1,
                                               traded_pair="XBTEUR")
    dca_runner = runner.DcaRunner(broker=BrokerStub(),
                                  dca_configuration=dca_configuration)

    dca_runner.run()
    prices = model.PriceHistory().get_prices()
    amounts_spent = model.Portfolio().get_amounts_spent()

    assert amounts_spent == [20]
    assert prices == [200]

    dca_runner.run()

    prices = model.PriceHistory().get_prices()
    total_spent = model.Portfolio().get_amounts_spent()

    assert total_spent == [20]
    assert prices == [200, 300]

    dca_runner.run()

    prices = model.PriceHistory().get_prices()
    total_spent = model.Portfolio().get_amounts_spent()

    assert total_spent == [20]
    assert prices == [200, 300, 250]

    dca_runner.run()

    prices = model.PriceHistory().get_prices()
    total_spent = model.Portfolio().get_amounts_spent()

    assert total_spent == [20, 21 + 22 + 23]
    assert prices == [200, 300, 250, 150]
