import typing
import mapper.mapper as mapper

DB = "db/price_history_pickle_db"
DB_TEST = "db/price_history_pickle_db_test.json"
PRICES_HISTORY_KEY = "prices_history"


class PriceHistoryMapper(mapper.Mapper):
    def __init__(self):
        super().__init__(db_test=DB_TEST, db=DB)

    def _save(self, price: float, time: float):
        if not self._db.get(PRICES_HISTORY_KEY):
            self._db.lcreate(PRICES_HISTORY_KEY)

        self._db.ladd(PRICES_HISTORY_KEY, price)
        return self._save_timestamp(time)

    def get_prices(self) -> typing.List[float]:
        if not self._db.get(PRICES_HISTORY_KEY):
            return []

        return self._db.lgetall(PRICES_HISTORY_KEY)
