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

    @staticmethod
    def _get_min_price(price_history):
        return min((min_val, min_index) for (min_index, min_val) in enumerate(price_history[0: -1]))
