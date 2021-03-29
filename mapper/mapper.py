import os
import constants
import pickledb
import typing
import abc
import time

TIMESTAMPS_KEY = "timestamps"


class Mapper(abc.ABC):
    def __init__(self):
        self._env = os.getenv(constants.ENV, constants.TEST_ENV)
        self._db_location: typing.Optional[str] = None
        self._db: typing.Optional[pickledb.PickleDB] = None

    def _get_db_location(self, db_test: str, db_production: str) -> str:
        if self._env == constants.TEST_ENV:
            return db_test
        elif self._env == constants.PRODUCTION_ENV:
            return db_production
        return db_test

    def _save_timestamp(self, timestamp: float = time.time()):
        if not self._db.get(TIMESTAMPS_KEY):
            self._db.lcreate(TIMESTAMPS_KEY)

        self._db.ladd(TIMESTAMPS_KEY, timestamp)
        return time
