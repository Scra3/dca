import main as main


def test_amount_to_spend__returns_initialise_price_when_there_is_only_one_price():
    amount = main.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10])
    assert amount == 20


def test_amount_to_spend__returns_initialise_price_and_step_price_sum():
    amount = main.Dca(price_initialisation=20, step_price=5).compute_amount_to_spend([10, 11])
    assert amount == 25


def test_amount_to_spend__returns_initialise_price_and_step_price_sum_with_3_prices():
    amount = main.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 11, 5])
    assert amount == 22
