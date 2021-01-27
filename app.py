import price_history as ph
import portfolio as portfolio
import dca as algo


class App:
    def __init__(self, price_history: ph.PriceHistory):
        self._price_history = price_history
        self._portfolio = portfolio.Portfolio()
        self._dca = algo.Dca(price_initialisation=20, step_price=1)

    def run(self):
        current_price = self._price_history.get_current_bitcoin_price()
        history = self._price_history.save_price(current_price).get_prices()
        amount_to_spent = self._dca.compute_amount_to_spend(prices_history=history, total_spent=100)
        self._portfolio.save_spent(amount_to_spent)
