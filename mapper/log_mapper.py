import mapper.mapper as mapper
import typing

DB = "db/log_pickle_db"
DB_TEST = "db/log_pickle_db_test.json"
MESSAGES_KEY = "messages"
TYPES_KEY = "types"


class LogMapper(mapper.Mapper):
    def __init__(self, log_type: str, message: str, timestamp: typing.Optional[float]):
        self._log_type: str = log_type
        self._message: str = message
        self._timestamp: typing.Optional[float] = timestamp

    def save(self) -> float:
        db = mapper.Mapper.load_db(db_test=DB_TEST, db=DB)

        if not db.get(MESSAGES_KEY):
            db.lcreate(MESSAGES_KEY)
        if not db.get(TYPES_KEY):
            db.lcreate(TYPES_KEY)

        db.ladd(MESSAGES_KEY, self._message)
        db.ladd(TYPES_KEY, self._log_type)
        return self._save_timestamp(db, self._timestamp)

    @staticmethod
    def drop_db():
        location = mapper.Mapper._get_db_location(db_test=DB_TEST, db=DB)
        mapper.Mapper._drop_db(location)
