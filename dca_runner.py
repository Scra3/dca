import time
import model
from model.log import Log


class DcaRunner:
    def __init__(self, broker: model.Broker, dca_configuration: model.DcaConfiguration):
        self._price_history = model.PriceHistory()
        self._portfolio = model.Portfolio()
        self._dca_configuration = dca_configuration
        self._dca = model.Dca(config=dca_configuration)
        self._broker = broker

    def run(self):
        current_price = self._broker.get_current_pair_price(self._dca_configuration.traded_pair)
        prices = self._price_history.get_prices()
        total_spent = self._portfolio.get_total_spent()
        amount_to_spent = self._dca.compute_amount_to_spend(current_price=current_price,
                                                            prices_history=prices,
                                                            total_spent=total_spent)
        timestamp = time.time()
        self._price_history.save(price=current_price, timestamp=timestamp)

        if amount_to_spent > 0:
            self._broker.send_buy_order(price=current_price, amount_to_spent=amount_to_spent,
                                        traded_pair=self._dca_configuration.traded_pair)
            model.Order().save(amount_to_spent, current_price, timestamp)
            Log().success(
                f"buy order is sent - amount_to_spent={amount_to_spent}, current_price={current_price}").save()
        else:
            Log().info(
                f"buy order is not sent - amount_to_spent={amount_to_spent}, current_price={current_price}").save()
