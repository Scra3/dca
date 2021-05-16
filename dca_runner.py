import time
import model
from model.log import Log


class DcaRunner:
    def __init__(self, broker: model.Broker, dca_configuration: model.DcaConfiguration):
        self._dca_configuration = dca_configuration
        self._dca = model.Dca(config=dca_configuration)
        self._broker = broker

    def run(self):
        current_price = self._broker.get_current_pair_price(
            self._dca_configuration.traded_pair
        )
        prices = model.PriceHistory.get_prices()
        total_spent = model.Portfolio.get_total_spent()
        amount_to_spend = self._dca.compute_amount_to_spend(
            current_price=current_price, prices_history=prices, total_spent=total_spent
        )
        timestamp = time.time()
        model.PriceHistory(price=current_price, timestamp=timestamp).save()

        if amount_to_spend > 0:
            self._broker.send_buy_order(
                traded_pair=self._dca_configuration.traded_pair,
                price=current_price,
                amount_to_spend=amount_to_spend,
            )
            model.Order(
                amount_to_spend,
                current_price,
                model.OrderType.BUY,
                timestamp,
            ).save()
            Log.success(
                f"buy order is sent - amount_to_spend={amount_to_spend}, current_price={current_price}"
            ).save()
        else:
            Log.info(
                f"buy order is not sent - amount_to_spend={amount_to_spend}, current_price={current_price}"
            ).save()
