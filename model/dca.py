import typing
import json


class DcaConfiguration:
    def __init__(self,
                 price_initialisation: float,
                 step_price: float,
                 traded_pair: typing.Optional[str] = None,
                 force_buy_under_price: typing.Optional[float] = None,
                 max_amount_to_spend: typing.Optional[float] = None,
                 max_total_amount_to_spend: typing.Optional[float] = None):
        self.price_initialisation = price_initialisation
        self.step_price = step_price
        self.force_buy_under_price = force_buy_under_price
        self.max_amount_to_spend = max_amount_to_spend
        self.max_total_amount_to_spend = max_total_amount_to_spend
        self.traded_pair = traded_pair

    @classmethod
    def serialise(cls, json_as_str: str):
        return json.loads(json_as_str, object_hook=DcaConfiguration.as_dca_configuration)

    @staticmethod
    def as_dca_configuration(dct):
        return DcaConfiguration(price_initialisation=dct.get("price_initialisation"),
                                step_price=dct.get("step_price"),
                                traded_pair=dct.get("traded_pair"),
                                force_buy_under_price=dct.get("force_buy_under_price"),
                                max_amount_to_spend=dct.get("max_amount_to_spend"),
                                max_total_amount_to_spend=dct.get("max_total_amount_to_spend"))


class Dca:
    def __init__(self, config: DcaConfiguration):
        self._config = config

        if self._config.max_amount_to_spend is not None \
                and self._config.price_initialisation > self._config.max_amount_to_spend:
            raise Exception('price_initialisation must be bigger or equal than max_amount_to_spend')

        if self._config.max_total_amount_to_spend is not None and \
                self._config.price_initialisation > self._config.max_total_amount_to_spend:
            raise Exception('price_initialisation must be bigger or equal than max_total_amount_to_spend')

    def compute_amount_to_spend(self, current_price: float, prices_history: typing.List[float],
                                total_spent: typing.Optional[float] = 0) -> float:
        if len(prices_history) == 0:
            return self._config.price_initialisation

        count_price = len(prices_history)

        force_to_buy = self._config.force_buy_under_price is not None and self._config.force_buy_under_price >= current_price
        if force_to_buy:
            next_amount = count_price * self._config.step_price + self._config.price_initialisation
        else:
            min_price, min_index = Dca._get_min_price(prices_history)
            if min_price < current_price:
                return 0.0

            prices = prices_history[min_index + 1:count_price]
            prices.append(current_price)
            next_amount = len(prices) * self._config.price_initialisation

            for index, _ in enumerate(prices_history[min_index:count_price]):
                next_amount += (count_price - index) * self._config.step_price

        next_total_spent = total_spent + next_amount
        if self._config.max_total_amount_to_spend is not None and self._config.max_total_amount_to_spend <= next_total_spent:
            next_amount = self._config.max_total_amount_to_spend - total_spent
            return next_amount if next_amount >= 0 else 0

        if self._config.max_amount_to_spend is not None and self._config.max_amount_to_spend <= next_amount:
            return self._config.max_amount_to_spend

        return next_amount

    @staticmethod
    def _get_min_price(prices_history: typing.List[float]) -> typing.Tuple[float, int]:
        """
            it returns the min price from a list
            _get_min_price([8, 8, 8, 8]) => (8, 3)
        """
        price, index = min((x, -i) for i, x in enumerate(prices_history))
        return price, -index
