import mapper
import typing


class Order(mapper.OrdersMapper):
    def __init__(self, amount: float = None, price: float = None, timestamp: float = None):
        super().__init__()
        self._amount: typing.Optional[float] = amount
        self._price: typing.Optional[float] = price
        self._timestamp: typing.Optional[float] = timestamp

    def save(self):
        self._timestamp = self._save(self._amount, self._price, self._timestamp)
