import model
from fixtures import drop_databases_after_test


def test_save_one_price_and_get_prices_persisted(drop_databases_after_test):
    model.PriceHistory(price=10).save()

    saved_prices = model.PriceHistory().get_prices()

    assert saved_prices == [10]


def test_save_several_prices_and_get_prices_persisted(drop_databases_after_test):
    model.PriceHistory(price=10).save()
    model.PriceHistory(price=20).save()

    saved_prices = model.PriceHistory().get_prices()
    assert saved_prices == [10, 20]
