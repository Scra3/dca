import pytest
import model


@pytest.fixture
def drop_databases_after_test():
    yield
    model.PriceHistory().drop_db()


def test_save_one_price_and_get_prices_persisted(drop_databases_after_test):
    model.PriceHistory().save_price(10)

    saved_prices = model.PriceHistory().get_prices()

    assert saved_prices == [10]


def test_save_several_prices_and_get_prices_persisted(drop_databases_after_test):
    model.PriceHistory().save_price(10)
    model.PriceHistory().save_price(20)

    saved_prices = model.PriceHistory().get_prices()
    assert saved_prices == [10, 20]
