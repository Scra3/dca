import pickledb
import os
import config as config

PORTFOLIO_DB = "db/portfolio_pickle_db"
PORTFOLIO_DB_TEST = "db/portfolio_pickle_db_test"
TOTAL_SPENT_NAME = "total_spent_name"


class PortfolioMapper:
    def __init__(self):
        self._env = os.getenv(config.ENV, config.TEST_ENV)
        self._db: pickledb.PickleDB = self._load_db()

    def drop_db(self):
        location = self._get_location_db()
        if os.path.exists(location):
            os.remove(location)

    def _load_db(self, dump: bool = True) -> pickledb.PickleDB:
        return pickledb.load(self._get_location_db(), dump)

    def _get_location_db(self) -> str:
        if self._env == config.TEST_ENV:
            return PORTFOLIO_DB_TEST

        return PORTFOLIO_DB

    def save_spent(self, price: float):
        if not self._db.get(TOTAL_SPENT_NAME):
            self._db.lcreate(TOTAL_SPENT_NAME)

        self._db.ladd(TOTAL_SPENT_NAME, price)
        return self

    def get_total_spent(self) -> float:
        if not self._db.get(TOTAL_SPENT_NAME):
            return 0

        return sum(self._db.lgetall(TOTAL_SPENT_NAME))

    def get_amounts_spent(self) -> float:
        if not self._db.get(TOTAL_SPENT_NAME):
            return 0

        return self._db.lgetall(TOTAL_SPENT_NAME)