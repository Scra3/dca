import pickledb
import mapper.mapper as mapper
import os
import typing

PORTFOLIO_DB = "db/orders_pickle_db"
PORTFOLIO_DB_TEST = "db/orders_pickle_db_test.json"
AMOUNTS_SPENT_KEY = "amounts_spent"
BUYING_PRICES_KEY = "prices"


class OrdersMapper(mapper.Mapper):
    def __init__(self):
        super().__init__()
        self._db_location = self._get_db_location(db_test=PORTFOLIO_DB_TEST, db_production=PORTFOLIO_DB)
        self._db = self._load_db()

    def drop_db(self):
        if os.path.exists(self._db_location):
            os.remove(self._db_location)

    def _load_db(self, dump: bool = True) -> pickledb.PickleDB:
        return pickledb.load(self._db_location, dump)

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
