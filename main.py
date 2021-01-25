import typing


class Dca:
    def __init__(self, price_initialisation: float):
        self.price_initialisation = price_initialisation

    def compute_amount_to_spend(self, history: typing.List[float]) -> float:
        return self.price_initialisation


if __name__ == '__main__':
    Dca().compute_amount_to_spend([10])
