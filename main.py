import typing


class Dca:
    def __init__(self, price_initialisation: float, step_price: float):
        self.price_initialisation = price_initialisation
        self.step_price = step_price

    def compute_amount_to_spend(self, price_history: typing.List[float]) -> float:
        if len(price_history) == 1:
            return self.price_initialisation

        min_val, min_index = min((min_val, min_index) for (min_index, min_val) in enumerate(price_history[0: -1]))

        if len(price_history) >= 2 and min_val < price_history[-1]:
            return 0.0

        last_index = len(price_history) - 1
        if min_index < last_index:
            prices = price_history[min_index + 1:last_index + 1]
            next_amount = len(prices) * self.price_initialisation

            init = (len(price_history) - 1)
            for idx, price in enumerate(price_history[min_index:last_index]):
                next_amount += (init - idx) * self.step_price

        else:
            next_amount = (len(price_history) - 1) * self.step_price + self.price_initialisation

        return next_amount


if __name__ == '__main__':
    pass
