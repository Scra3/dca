import pickledb
import os
import config as config

PRICE_HISTORY_DB = "db/portfolio_pickle_db"
PORTFOLIO_DB_TEST = "db/portfolio_pickle_db_test"
TOTAL_SPENT_NAME = "total_spent_name"


class PortfolioMapper:

    @staticmethod
    def drop_db():
        os.remove(PORTFOLIO_DB_TEST)

    @staticmethod
    def _load_db(dump: bool = True):
        env = os.getenv('ENV', "production")

        if env == config.TEST_ENV:
            return pickledb.load(PORTFOLIO_DB_TEST, dump)

        return pickledb.load(PRICE_HISTORY_DB, dump)

    @staticmethod
    def save_spent(price: float):
        db = PortfolioMapper._load_db()
        if not db.get(TOTAL_SPENT_NAME):
            db.lcreate(TOTAL_SPENT_NAME)

        db.ladd(TOTAL_SPENT_NAME, price)

    @staticmethod
    def get_total_spend() -> float:
        db = PortfolioMapper._load_db(dump=False)

        return sum(db.lgetall(TOTAL_SPENT_NAME))
