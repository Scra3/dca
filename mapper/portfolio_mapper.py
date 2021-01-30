import pickledb
import mapper.mapper as mapper
import os

PORTFOLIO_DB = "db/portfolio_pickle_db"
PORTFOLIO_DB_TEST = "db/portfolio_pickle_db_test"
TOTAL_SPENT_NAME = "total_spent_name"


class PortfolioMapper(mapper.Mapper):
    def __init__(self):
        super().__init__()
        self._db_location = self._get_location_db(db_test=PORTFOLIO_DB_TEST, db_production=PORTFOLIO_DB)
        self._db: pickledb.PickleDB = self._load_db()

    def drop_db(self):
        if os.path.exists(self._db_location):
            os.remove(self._db_location)

    def _load_db(self, dump: bool = True) -> pickledb.PickleDB:
        return pickledb.load(self._db_location, dump)

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
