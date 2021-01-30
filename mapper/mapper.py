import os
import config as config


class Mapper:
    def __init__(self):
        self._env = os.getenv(config.ENV, config.TEST_ENV)

    def _get_location_db(self, db_test: str, db_production: str) -> str:
        if self._env == config.TEST_ENV:
            return db_test
        elif self._env == config.PRODUCTION_ENV:
            return db_production
        return db_test
