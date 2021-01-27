import price_history as ph
import portfolio as portfolio
import dca as algo


class App:

    @staticmethod
    def run():
        current_price = ph.PriceHistory.get_current_bitcoin_price()
        ph.PriceHistory.save_price(current_price)
        history = ph.PriceHistory.get_prices()
        dca = algo.Dca(price_initialisation=20, step_price=1)
        amount_to_spent = dca.compute_amount_to_spend(prices_history=history, total_spent=100)

        portfolio.Portfolio.save_spent(amount_to_spent)
