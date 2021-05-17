import mapper
import enum
import typing


class OrderType(enum.Enum):
    BUY = "buy"
    SELL = "sell"


class Order(mapper.OrdersMapper):
    def __init__(
        self,
        amount: float,
        price: float,
        order_type: OrderType,
        timestamp: typing.Optional[float] = None,
    ):
        super().__init__(amount, price, order_type.value, timestamp)
