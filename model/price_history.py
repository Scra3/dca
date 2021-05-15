import mapper
import typing


class PriceHistory(mapper.PriceHistoryMapper):
    def __init__(self, price: float = None, timestamp: float = None):
        super().__init__()
        self._price: typing.Optional[float] = price
        self._timestamp: typing.Optional[float] = timestamp

    def save(self):
        self._timestamp = self._save(self._price, self._timestamp)
