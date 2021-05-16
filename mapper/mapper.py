import os
import constants
import pickledb
import typing
import abc
import time

TIMESTAMPS_KEY = "timestamps"


class Mapper(abc.ABC):
    def __init__(self, db_test, db):
        self._db_location: typing.Optional[str] = self._get_db_location(
            db_test=db_test, db=db
        )
        self._db: typing.Optional[pickledb.PickleDB] = self._load_db()

    @staticmethod
    def _get_db_location(db_test: str, db: str) -> str:
        env = os.getenv(constants.ENV, constants.TEST_ENV)
        if env == constants.TEST_ENV:
            return db_test

        if env == constants.PRODUCTION_ENV:
            return db

        return db_test

    def _save_timestamp(self, timestamp: float = time.time()) -> float:
        if not self._db.get(TIMESTAMPS_KEY):
            self._db.lcreate(TIMESTAMPS_KEY)

        self._db.ladd(TIMESTAMPS_KEY, timestamp)
        return timestamp

    def drop_db(self):
        if os.path.exists(self._db_location):
            os.remove(self._db_location)

    def _load_db(self, dump: bool = True) -> pickledb.PickleDB:
        return pickledb.load(self._db_location, dump)
