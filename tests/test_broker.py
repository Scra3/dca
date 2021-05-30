import model


def test_get_current_bitcoin_price():
    price = model.Broker.get_current_pair_price(model.TradedPairMapping.ETHUSDC)
    assert price is not None


def test_get_current_ethereum_price():
    price = model.Broker.get_current_pair_price(model.TradedPairMapping.ETHUSDT)
    assert price is not None


def test__compute_volume_to_buy():
    price = model.Broker._compute_volume_to_buy(amount_to_spend=10, price=5)
    assert price == 2


def test__compute_volume_to_buy_with_big_float():
    price = model.Broker._compute_volume_to_buy(amount_to_spend=4, price=34060.17)
    assert price == 0.00011743922593457403
