import mapper
import typing


class Order(mapper.OrdersMapper):
    def __init__(self, amount: float = None, price: float = None):
        super().__init__()
        self._amount: typing.Optional[float] = amount
        self._price: typing.Optional[float] = price
        self._timestamp: typing.Optional[float] = None

    def save(self, amount: float = None, price: float = None, timestamp: float = None):
        if price is None:
            price = self._price
        if amount is None:
            amount = self._amount

        self._timestamp = self._save(amount, price, timestamp)
