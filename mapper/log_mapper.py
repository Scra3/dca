import pickledb
import typing
import os
import mapper.mapper as mapper

LOG = "db/log_pickle_db"
LOG_TEST = "db/log_pickle_db_test.json"
MESSAGES_KEY = "messages"
TYPES_KEY = "types"


class LogMapper(mapper.Mapper):
    def __init__(self):
        super().__init__()
        self._db_location = self._get_db_location(db_test=LOG_TEST, db_production=LOG)
        self._db = self._load_db()

    def drop_db(self):
        if os.path.exists(self._db_location):
            os.remove(self._db_location)

    def _load_db(self, dump: bool = True) -> pickledb.PickleDB:
        return pickledb.load(self._db_location, dump)

    def _save_log(self, log_type: str, message: str) -> float:
        if not self._db.get(MESSAGES_KEY):
            self._db.lcreate(MESSAGES_KEY)
        if not self._db.get(TYPES_KEY):
            self._db.lcreate(TYPES_KEY)

        self._db.ladd(MESSAGES_KEY, message)
        self._db.ladd(TYPES_KEY, log_type)
        return self._save_timestamp()
