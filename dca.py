import typing


class Dca:
    def __init__(self,
                 price_initialisation: float,
                 step_price: float,
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

    def compute_amount_to_spend(self, current_price: float, prices_history: typing.List[float],
                                total_spent: typing.Optional[float] = 0) -> float:
        current_price = prices_history[-1]
        prices_history = prices_history[:-1]
        if len(prices_history) == 0:
            return self.price_initialisation

        count_price = len(prices_history)

        force_to_buy = self.force_buy_under_price is not None and self.force_buy_under_price >= current_price
        if force_to_buy:
            next_amount = count_price * self.step_price + self.price_initialisation
        else:
            min_price, min_index = Dca._get_min_price(prices_history)
            if min_price < current_price:
                return 0.0

            prices = prices_history[min_index + 1:count_price]
            prices.append(current_price)
            next_amount = len(prices) * self.price_initialisation

            for index, _ in enumerate(prices_history[min_index:count_price + 1]):
                next_amount += (count_price - index) * self.step_price

        next_total_spent = total_spent + next_amount
        if self.max_total_amount_to_spend is not None and self.max_total_amount_to_spend <= next_total_spent:
            next_amount = self.max_total_amount_to_spend - total_spent
            return next_amount if next_amount >= 0 else 0

        if self.max_amount_to_spend is not None and self.max_amount_to_spend <= next_amount:
            return self.max_amount_to_spend

        return next_amount

    @staticmethod
    def get_average_price(total_spent: float, balance: float) -> float:
        return total_spent / balance

    @staticmethod
    def _get_min_price(prices_history) -> typing.Tuple[float, int]:
        """
            it returns the min price from a list
            _get_min_price([8, 8, 8, 8]) => (8, 2)
        """
        price, index = min((x, -i) for i, x in enumerate(prices_history))
        return price, -index
