import mapper.mapper as mapper
import typing

DB = "db/log_pickle_db"
DB_TEST = "db/log_pickle_db_test.json"
MESSAGES_KEY = "messages"
TYPES_KEY = "types"


class LogMapper(mapper.Mapper):
    def __init__(self, log_type: str, message: str, timestamp: float):
        super().__init__(db_test=DB_TEST, db=DB)
        self._log_type: typing.Optional[str] = log_type
        self._message: typing.Optional[str] = message
        self._timestamp: typing.Optional[float] = timestamp

    def save(self) -> float:
        if not self._db.get(MESSAGES_KEY):
            self._db.lcreate(MESSAGES_KEY)
        if not self._db.get(TYPES_KEY):
            self._db.lcreate(TYPES_KEY)

        self._db.ladd(MESSAGES_KEY, self._message)
        self._db.ladd(TYPES_KEY, self._log_type)
        return self._save_timestamp()
