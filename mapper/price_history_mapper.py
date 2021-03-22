import pickledb
import typing
import os
import config as config
import mapper.mapper as mapper

PRICE_HISTORY_DB = "db/price_history_pickle_db"
PRICE_HISTORY_DB_TEST = "db/price_history_pickle_db_test"
PRICES_HISTORY_KEY = "prices_history"


class PriceHistoryMapper(mapper.Mapper):
    def __init__(self):
        super().__init__()
        self._db_location = self._get_location_db(db_test=PRICE_HISTORY_DB_TEST, db_production=PRICE_HISTORY_DB)
        self._db: pickledb.PickleDB = self._load_db()

    def drop_db(self):
        if os.path.exists(self._db_location):
            os.remove(self._db_location)

    def _load_db(self, dump: bool = True) -> pickledb.PickleDB:
        return pickledb.load(self._db_location, dump)

    def save_price(self, price: float):
        if not self._db.get(PRICES_HISTORY_KEY):
            self._db.lcreate(PRICES_HISTORY_KEY)

        self._db.ladd(PRICES_HISTORY_KEY, price)
        return self

    def get_prices(self) -> typing.List[float]:
        if not self._db.get(PRICES_HISTORY_KEY):
            return []

        return self._db.lgetall(PRICES_HISTORY_KEY)
