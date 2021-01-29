import model


class DcaRunner:
    def __init__(self, price_history: model.PriceHistory, dca: model.Dca):
        self._price_history = price_history
        self._portfolio = model.Portfolio()
        self._dca = dca

    def run(self):
        current_price = self._price_history.get_current_bitcoin_price()
        history = self._price_history.get_prices()
        amount_to_spent = self._dca.compute_amount_to_spend(current_price=current_price, prices_history=history,
                                                            total_spent=self._portfolio.get_total_spent())
        self._portfolio.save_spent(amount_to_spent)
        self._price_history.save_price(current_price)
