import pickledb
import typing
import os
import config as config

PRICE_HISTORY_DB = "db/price_history_pickle_db"
PRICE_HISTORY_DB_TEST = "db/price_history_pickle_db_test"
PRICES_HISTORY_NAME = "prices_history_name"


class PriceHistoryMapper:
    def __init__(self):
        self._env = os.getenv('ENV', "production")
        self._db: pickledb.PickleDB = self._load_db()

    def drop_db(self):
        os.remove(self._get_location_db())

    def _load_db(self, dump: bool = True) -> pickledb.PickleDB:
        return pickledb.load(self._get_location_db(), dump)

    def _get_location_db(self):
        if self._env == config.TEST_ENV:
            return PRICE_HISTORY_DB_TEST

        return PRICE_HISTORY_DB

    def save_price(self, price: float):
        if not self._db.get(PRICES_HISTORY_NAME):
            self._db.lcreate(PRICES_HISTORY_NAME)

        self._db.ladd(PRICES_HISTORY_NAME, price)
        return self

    def get_prices(self) -> typing.List[float]:
        if not self._db.get(PRICES_HISTORY_NAME):
            return []

        return self._db.lgetall(PRICES_HISTORY_NAME)
