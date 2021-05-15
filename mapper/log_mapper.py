import mapper.mapper as mapper

DB = "db/log_pickle_db"
DB_TEST = "db/log_pickle_db_test.json"
MESSAGES_KEY = "messages"
TYPES_KEY = "types"


class LogMapper(mapper.Mapper):
    def __init__(self):
        super().__init__(db_test=DB_TEST, db=DB)

    def _save_log(self, log_type: str, message: str) -> float:
        if not self._db.get(MESSAGES_KEY):
            self._db.lcreate(MESSAGES_KEY)
        if not self._db.get(TYPES_KEY):
            self._db.lcreate(TYPES_KEY)

        self._db.ladd(MESSAGES_KEY, message)
        self._db.ladd(TYPES_KEY, log_type)
        return self._save_timestamp()
