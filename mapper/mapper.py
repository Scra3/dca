import os
import config as config
import pickledb
import typing
import abc

TIMESTAMPS_KEY = "timestamps"


class Mapper(abc.ABC):
    def __init__(self):
        self._env = os.getenv(config.ENV, config.TEST_ENV)
        self._db_location: typing.Optional[str] = None
        self._db: typing.Optional[pickledb.PickleDB] = None

    def _get_db_location(self, db_test: str, db_production: str) -> str:
        if self._env == config.TEST_ENV:
            return db_test
        elif self._env == config.PRODUCTION_ENV:
            return db_production
        return db_test

    def _save_timestamp(self, time: float):
        if not self._db.get(TIMESTAMPS_KEY):
            self._db.lcreate(TIMESTAMPS_KEY)

        self._db.ladd(TIMESTAMPS_KEY, time)
