import typing


class Dca:
    def __init__(self, price_initialisation: float, step_price: float,
                 force_buy_under_price: typing.Optional[float] = None,
                 max_amount_to_spend: typing.Optional[float] = None,
                 max_total_amount_to_spend: typing.Optional[float] = None):
        self.price_initialisation = price_initialisation
        self.step_price = step_price
        self.force_buy_under_price = force_buy_under_price
        self.max_amount_to_spend = max_amount_to_spend
        self.max_total_amount_to_spend = max_total_amount_to_spend

        if self.max_amount_to_spend is not None and self.price_initialisation > self.max_amount_to_spend:
            raise Exception('price_initialisation must be bigger or equal than max_amount_to_spend')

        if self.max_total_amount_to_spend is not None and self.price_initialisation > self.max_total_amount_to_spend:
            raise Exception('price_initialisation must be bigger or equal than max_total_amount_to_spend')

    def compute_amount_to_spend(self, price_history: typing.List[float]) -> float:
        if len(price_history) == 1:
            return self.price_initialisation

        last_index = len(price_history) - 1

        force_to_buy = self.force_buy_under_price is not None and self.force_buy_under_price >= price_history[-1]
        if force_to_buy:
            return last_index * self.step_price + self.price_initialisation

        min_price, min_index = Dca._get_min_price(price_history)

        if last_index and min_price < price_history[-1]:
            return 0.0

        prices = price_history[min_index + 1:last_index + 1]
        next_amount = len(prices) * self.price_initialisation

        for index, _ in enumerate(price_history[min_index:last_index]):
            next_amount += (last_index - index) * self.step_price

        total_spent = self.get_total_spent(price_history[0:-1])
        next_total_spent = total_spent + next_amount

        if self.max_total_amount_to_spend is not None and self.max_total_amount_to_spend <= next_total_spent:
            return self.max_total_amount_to_spend - total_spent

        if self.max_amount_to_spend is not None and self.max_amount_to_spend <= next_amount:
            return self.max_amount_to_spend

        return next_amount

    def get_total_spent(self, price_history: typing.List[float]) -> float:
        total: float = 0

        for index, _ in enumerate(price_history):
            total += self.compute_amount_to_spend(price_history[0:index + 1])
        return total

    def get_balance(self, price_history: typing.List[float]) -> float:
        total: float = 0

        for index, value in enumerate(price_history):
            amount = self.compute_amount_to_spend(price_history[0:index + 1])
            total = total + amount / value

        return total

    def get_average_amount(self, price_history: typing.List[float]) -> float:
        return self.get_total_spent(price_history) / self.get_balance(price_history)

    @staticmethod
    def _get_min_price(price_history):
        return min((min_val, min_index) for (min_index, min_val) in enumerate(price_history[0: -1]))
