import model


def test_get_current_bitcoin_price():
    price = model.Broker().get_current_pair_price("XBTEUR")
    assert price is not None
