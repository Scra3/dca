import pickledb
import typing
import os

PRICE_HISTORY_DB = "db/price_history_pickle_db"
PRICE_HISTORY_DB_TEST = "db/price_history_pickle_db_test"
PRICES_HISTORY_NAME = "prices_history_name"

TEST_ENV = "test"


class PriceHistoryMapper:

    @staticmethod
    def drop_db():
        os.remove(PRICE_HISTORY_DB_TEST)

    @staticmethod
    def _load_db(dump: bool = True):
        env = os.getenv('ENV', "production")

        if env == TEST_ENV:
            return pickledb.load(PRICE_HISTORY_DB_TEST, dump)

        return pickledb.load(PRICE_HISTORY_DB, dump)

    @staticmethod
    def save_price(price: float):
        db = PriceHistoryMapper._load_db()
        if not db.get(PRICES_HISTORY_NAME):
            db.lcreate(PRICES_HISTORY_NAME)

        db.ladd(PRICES_HISTORY_NAME, price)

    @staticmethod
    def get_prices() -> typing.List[float]:
        db = PriceHistoryMapper._load_db(dump=False)

        return db.lgetall(PRICES_HISTORY_NAME)
