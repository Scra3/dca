import model
from fixtures import drop_databases_after_test


def test_get_amount_spent(drop_databases_after_test):
    model.Order(amount=10, price=10).save()
    model.Order(amount=24.5, price=11).save()

    total_spent = model.Order().get_amounts_spent()

    assert total_spent == [10, 24.5]


def test_get_buying_prices(drop_databases_after_test):
    model.Order(amount=10, price=10).save()
    model.Order(amount=24.5, price=11).save()

    total_spent = model.Order().get_buying_prices()

    assert total_spent == [10, 11]
