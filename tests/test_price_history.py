import price_history as model


def test_get_current_bitcoin_price():
    price = model.PriceHistory.get_current_bitcoin_price()
    assert price is not None
