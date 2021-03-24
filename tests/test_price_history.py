import pytest
import model


@pytest.fixture
def drop_databases_after_test():
    yield
    model.PriceHistory().drop_db()


def test_save_one_price_and_get_prices_persisted(drop_databases_after_test):
    model.PriceHistory().save_price(price=10, time=10.0)

    saved_prices = model.PriceHistory().get_prices()

    assert saved_prices == [10]


def test_save_several_prices_and_get_prices_persisted(drop_databases_after_test):
    model.PriceHistory().save_price(price=10, time=10.0)
    model.PriceHistory().save_price(price=20, time=10.0)

    saved_prices = model.PriceHistory().get_prices()
    assert saved_prices == [10, 20]
