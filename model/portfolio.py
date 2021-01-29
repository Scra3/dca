import mapper
import model


class Portfolio(mapper.PortfolioMapper):
    def __init__(self):
        super().__init__()
        self._price_history: model.PriceHistory = model.PriceHistory()

    def get_average_price(self) -> float:
        return self.get_total_spent() / self.get_balance()

    def get_balance(self) -> float:
        balance = 0
        amounts_spent = self.get_amounts_spent()
        prices = self._price_history.get_prices()
        for index, _ in enumerate(prices):
            balance += amounts_spent[index] / prices[index]

        return balance
