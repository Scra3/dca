import typing
import mapper.mapper as mapper

DB = "db/price_history_pickle_db"
DB_TEST = "db/price_history_pickle_db_test.json"
PRICES_HISTORY_KEY = "prices_history"


class PriceHistoryMapper(mapper.Mapper):
    def __init__(self, price: float, timestamp: typing.Optional[float]):
        self._price: float = price
        self._timestamp: typing.Optional[float] = timestamp

    def save(self):
        db = mapper.Mapper.load_db(db_test=DB_TEST, db=DB)

        if not db.get(PRICES_HISTORY_KEY):
            db.lcreate(PRICES_HISTORY_KEY)

        db.ladd(PRICES_HISTORY_KEY, self._price)
        return self._save_timestamp(db, self._timestamp)

    @staticmethod
    def get_prices() -> typing.List[float]:
        db = mapper.Mapper.load_db(db_test=DB_TEST, db=DB)

        if not db.get(PRICES_HISTORY_KEY):
            return []

        return db.lgetall(PRICES_HISTORY_KEY)

    @staticmethod
    def drop_db():
        location = mapper.Mapper._get_db_location(db_test=DB_TEST, db=DB)
        mapper.Mapper._drop_db(location)
