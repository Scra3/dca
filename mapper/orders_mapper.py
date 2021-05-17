import typing

import mapper.mapper as mapper

DB = "db/orders_pickle_db"
DB_TEST = "db/orders_pickle_db_test.json"
AMOUNTS_SPENT_KEY = "amounts_spent"
BUYING_PRICES_KEY = "prices"
TYPE_KEY = "type"


class OrdersMapper(mapper.Mapper):
    def __init__(
        self,
        amount: float,
        price: float,
        order_type: str,
        timestamp: typing.Optional[float],
    ):
        self._amount: float = amount
        self._price: float = price
        self._timestamp: typing.Optional[float] = timestamp
        self._type: str = order_type

    def save(self) -> float:
        db = mapper.Mapper.load_db(db_test=DB_TEST, db=DB)

        if not db.get(AMOUNTS_SPENT_KEY):
            db.lcreate(AMOUNTS_SPENT_KEY)
        if not db.get(BUYING_PRICES_KEY):
            db.lcreate(BUYING_PRICES_KEY)
        if not db.get(TYPE_KEY):
            db.lcreate(TYPE_KEY)

        db.ladd(AMOUNTS_SPENT_KEY, self._amount)
        db.ladd(BUYING_PRICES_KEY, self._price)
        db.ladd(TYPE_KEY, self._type)

        self._timestamp = self._save_timestamp(db, self._timestamp)
        return self._timestamp

    @staticmethod
    def get_prices() -> typing.List[float]:
        db = mapper.Mapper.load_db(db_test=DB_TEST, db=DB)

        if not db.get(BUYING_PRICES_KEY):
            return []

        return db.lgetall(BUYING_PRICES_KEY)

    @staticmethod
    def get_volumes() -> typing.List[float]:
        db = mapper.Mapper.load_db(db_test=DB_TEST, db=DB)

        if not db.get(AMOUNTS_SPENT_KEY):
            return []

        return db.lgetall(AMOUNTS_SPENT_KEY)

    @staticmethod
    def get_orders_type() -> typing.List[str]:
        db = mapper.Mapper.load_db(db_test=DB_TEST, db=DB)

        if not db.get(TYPE_KEY):
            return []

        return db.lgetall(TYPE_KEY)

    @staticmethod
    def drop_db():
        location = mapper.Mapper._get_db_location(db_test=DB_TEST, db=DB)
        mapper.Mapper._drop_db(location)
