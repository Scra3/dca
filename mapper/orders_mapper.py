import pickledb
import mapper.mapper as mapper
import typing

DB = "db/orders_pickle_db"
DB_TEST = "db/orders_pickle_db_test.json"
AMOUNTS_SPENT_KEY = "amounts_spent"
BUYING_PRICES_KEY = "prices"


class OrdersMapper(mapper.Mapper):
    def __init__(self):
        super().__init__(db_test=DB_TEST, db=DB)

    def _save(self, amount: float, price: float, timestamp: float):
        if not self._db.get(AMOUNTS_SPENT_KEY):
            self._db.lcreate(AMOUNTS_SPENT_KEY)
        if not self._db.get(BUYING_PRICES_KEY):
            self._db.lcreate(BUYING_PRICES_KEY)

        self._db.ladd(AMOUNTS_SPENT_KEY, amount)
        self._db.ladd(BUYING_PRICES_KEY, price)
        return self._save_timestamp(timestamp)

    def get_buying_prices(self) -> typing.List[float]:
        if not self._db.get(BUYING_PRICES_KEY):
            return []

        return self._db.lgetall(BUYING_PRICES_KEY)

    def get_amounts_spent(self) -> typing.List[float]:
        if not self._db.get(AMOUNTS_SPENT_KEY):
            return []

        return self._db.lgetall(AMOUNTS_SPENT_KEY)
