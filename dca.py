import typing


class Dca:
    def __init__(self, price_initialisation: float, step_price: float):
        self.price_initialisation = price_initialisation
        self.step_price = step_price

    def compute_amount_to_spend(self, price_history: typing.List[float]) -> float:
        if len(price_history) == 1:
            return self.price_initialisation

        min_val, min_index = Dca._get_min_price(price_history)

        last_index = len(price_history) - 1

        if last_index and min_val < price_history[-1]:
            return 0.0

        prices = price_history[min_index + 1:last_index + 1]
        next_amount = len(prices) * self.price_initialisation

        for index, _ in enumerate(price_history[min_index:last_index]):
            next_amount += (last_index - index) * self.step_price

        return next_amount

    def get_total_spent(self, price_history: typing.List[float]):
        total: float = 0

        for index, _ in enumerate(price_history):
            total += self.compute_amount_to_spend(price_history[0:index + 1])
        return total

    def get_balance(self, price_history: typing.List[float]):
        total: float = 0

        for index, value in enumerate(price_history):
            amount = self.compute_amount_to_spend(price_history[0:index + 1])
            total = total + amount / value

        return total

    def get_average_amount(self, price_history: typing.List[float]):
        return self.get_total_spent(price_history) / self.get_balance(price_history)

    @staticmethod
    def _get_min_price(price_history):
        return min((min_val, min_index) for (min_index, min_val) in enumerate(price_history[0: -1]))
