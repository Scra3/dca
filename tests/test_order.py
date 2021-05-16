import model
from fixtures import drop_databases


def test_get_amount_spent(drop_databases):
    model.Order(amount=10, price=10).save()
    model.Order(amount=24.5, price=11).save()

    total_spent = model.Order().get_volumes()

    assert total_spent == [10, 24.5]


def test_get_prices(drop_databases):
    model.Order(amount=10, price=10).save()
    model.Order(amount=24.5, price=11).save()

    total_spent = model.Order().get_prices()

    assert total_spent == [10, 11]
