import mapper.mapper as mapper
import typing

DB = "db/orders_pickle_db"
DB_TEST = "db/orders_pickle_db_test.json"
AMOUNTS_SPENT_KEY = "amounts_spent"
BUYING_PRICES_KEY = "prices"
TYPE_KEY = "type"


class OrdersMapper(mapper.Mapper):
    def __init__(
        self, amount: float, price: float, timestamp: float, order_type: str
    ):
        super().__init__(db_test=DB_TEST, db=DB)
        self._amount: typing.Optional[float] = amount
        self._price: typing.Optional[float] = price
        self._timestamp: typing.Optional[float] = timestamp
        self._type: typing.Optional[str] = order_type

    def save(self) -> float:
        if not self._db.get(AMOUNTS_SPENT_KEY):
            self._db.lcreate(AMOUNTS_SPENT_KEY)
        if not self._db.get(BUYING_PRICES_KEY):
            self._db.lcreate(BUYING_PRICES_KEY)
        if not self._db.get(TYPE_KEY):
            self._db.lcreate(TYPE_KEY)

        self._db.ladd(AMOUNTS_SPENT_KEY, self._amount)
        self._db.ladd(BUYING_PRICES_KEY, self._price)
        self._db.ladd(TYPE_KEY, self._type)

        self._timestamp = self._save_timestamp(self._timestamp)
        return self._timestamp

    def get_prices(self) -> typing.List[float]:
        if not self._db.get(BUYING_PRICES_KEY):
            return []

        return self._db.lgetall(BUYING_PRICES_KEY)

    def get_volumes(self) -> typing.List[float]:
        if not self._db.get(AMOUNTS_SPENT_KEY):
            return []

        return self._db.lgetall(AMOUNTS_SPENT_KEY)

    def get_orders_type(self) -> typing.List[str]:
        if not self._db.get(TYPE_KEY):
            return []

        return self._db.lgetall(TYPE_KEY)
