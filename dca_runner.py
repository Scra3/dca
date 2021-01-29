import model


class DcaRunner:
    def __init__(self, broker: model.Broker, dca_configuration: model.DcaConfiguration):
        self._price_history = model.PriceHistory()
        self._portfolio = model.Portfolio()
        self._dca_configuration = dca_configuration
        self._dca = model.Dca(config=dca_configuration)
        self._broker = broker

    def run(self):
        current_price = self._broker.get_current_pair_price(self._dca_configuration.traded_pair)
        history = self._price_history.get_prices()
        amount_to_spent = self._dca.compute_amount_to_spend(current_price=current_price, prices_history=history,
                                                            total_spent=self._portfolio.get_total_spent())
        self._portfolio.save_spent(amount_to_spent)
        self._broker.send_buy_order(price=current_price, amount_to_spent=amount_to_spent,
                                    pair=self._dca_configuration.traded_pair)
        self._price_history.save_price(current_price)
