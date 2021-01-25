import main as main


def test_amount_to_spend__returns_initialise_price():
    amount = main.Dca(price_initialisation=20).compute_amount_to_spend([10])
    assert amount == 20
