import model


class Portfolio:
    def __init__(self):
        super().__init__()
        self._order: model.Order = model.Order()

    @staticmethod
    def get_average_price() -> float:
        return Portfolio.get_total_spent() / Portfolio.get_balance()

    @staticmethod
    def get_balance() -> float:
        volumes = model.Order().get_volumes()
        prices = model.Order().get_prices()
        return sum([volumes[index] / prices[index] for index, _ in enumerate(prices)])

    @staticmethod
    def get_total_spent() -> float:
        return sum(model.Order().get_volumes())
