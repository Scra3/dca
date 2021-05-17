import abc
import os
import time
import typing

import pickledb

import constants

TIMESTAMPS_KEY = "timestamps"


class Mapper(abc.ABC):
    @staticmethod
    def _get_db_location(db_test: str, db: str) -> str:
        env = os.getenv(constants.ENV, constants.TEST_ENV)
        dir_path = os.path.dirname(os.path.realpath(__file__))

        if env == constants.TEST_ENV:
            return f"{dir_path}/../{db_test}"

        if env == constants.PRODUCTION_ENV:
            return f"{dir_path}/../{db}"

        return db_test

    @staticmethod
    def _save_timestamp(db: pickledb.PickleDB, timestamp: float = time.time()) -> float:
        if not db.get(TIMESTAMPS_KEY):
            db.lcreate(TIMESTAMPS_KEY)

        db.ladd(TIMESTAMPS_KEY, timestamp)
        return timestamp

    @staticmethod
    def _drop_db(location: str):
        if os.path.exists(location):
            os.remove(location)

    @staticmethod
    def load_db(db_test: str, db: str, dump: bool = True) -> pickledb.PickleDB:
        return pickledb.load(Mapper._get_db_location(db_test=db_test, db=db), dump)
