import pytest
import model


@pytest.fixture
def drop_databases_after_test():
    yield
    model.Order().drop_db()
    model.PriceHistory().drop_db()
    model.Log().drop_db()
