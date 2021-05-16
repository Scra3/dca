import mapper
import typing


class PriceHistory(mapper.PriceHistoryMapper):
    def __init__(
        self,
        price: typing.Optional[float] = None,
        timestamp: typing.Optional[float] = None,
    ):
        super().__init__(price, timestamp)
