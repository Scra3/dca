import typing
import mapper.mapper as mapper

DB = "db/price_history_pickle_db"
DB_TEST = "db/price_history_pickle_db_test.json"
PRICES_HISTORY_KEY = "prices_history"


class PriceHistoryMapper(mapper.Mapper):
    def __init__(
        self, price: typing.Optional[float], timestamp: typing.Optional[float]
    ):
        super().__init__(db_test=DB_TEST, db=DB)
        self._price: typing.Optional[float] = price
        self._timestamp: typing.Optional[float] = timestamp

    def save(self):
        if not self._db.get(PRICES_HISTORY_KEY):
            self._db.lcreate(PRICES_HISTORY_KEY)

        self._db.ladd(PRICES_HISTORY_KEY, self._price)
        return self._save_timestamp(self._timestamp)

    def get_prices(self) -> typing.List[float]:
        if not self._db.get(PRICES_HISTORY_KEY):
            return []

        return self._db.lgetall(PRICES_HISTORY_KEY)
