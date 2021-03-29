import model


class Portfolio:
    def __init__(self):
        super().__init__()
        self._order: model.Order = model.Order()

    def get_average_price(self) -> float:
        return self.get_total_spent() / self.get_balance()

    def get_balance(self) -> float:
        balance = 0
        amounts_spent = self._order.get_amounts_spent()
        prices = self._order.get_buying_prices()
        for index, _ in enumerate(prices):
            balance += amounts_spent[index] / prices[index]

        return balance

    def get_total_spent(self) -> float:
        return sum(self._order.get_amounts_spent())
