import typing

import mapper


class PriceHistory(mapper.PriceHistoryMapper):
    def __init__(
        self,
        price: float,
        timestamp: typing.Optional[float] = None,
    ):
        super().__init__(price, timestamp)
