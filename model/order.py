import mapper
import enum


class OrderType(enum.Enum):
    BUY = "buy"
    SELL = "sell"


class Order(mapper.OrdersMapper):
    def __init__(
        self,
        amount: float = None,
        price: float = None,
        timestamp: float = None,
        order_type: OrderType = None,
    ):
        super().__init__(
            amount, price, timestamp, None if order_type is None else order_type.value
        )
