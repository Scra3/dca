import typing


class Dca:
    def __init__(self, price_initialisation: float, step_price: float):
        self.price_initialisation = price_initialisation
        self.step_price = step_price

    def compute_amount_to_spend(self, price_history: typing.List[float]) -> float:
        if len(price_history) >= 2 and price_history[-1] > price_history[-2]:
            return 0

        next_amount = (len(price_history) - 1) * self.step_price + self.price_initialisation

        return next_amount


if __name__ == '__main__':
    pass
