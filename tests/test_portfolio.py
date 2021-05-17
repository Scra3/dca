from fixtures import drop_databases

import model


def test_get_average_price(drop_databases):
    model.Order(amount=10, price=10, order_type=model.OrderType.BUY).save()

    price = model.Portfolio.get_average_price()

    assert price == 10


def test_get_balance(drop_databases):
    model.Order(amount=1, price=10, order_type=model.OrderType.BUY).save()
    model.Order(amount=1, price=10, order_type=model.OrderType.BUY).save()

    balance = model.Portfolio.get_balance()

    assert balance == 0.1 + 0.1
