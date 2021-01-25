import main as main


def test_amount_to_spend__returns_initialise_price_when_there_is_only_one_price():
    amount = main.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10])
    assert amount == 20


def test_amount_to_spend__returns_initialise_price_and_step_price_sum():
    amount = main.Dca(price_initialisation=20, step_price=5).compute_amount_to_spend([10, 8])
    assert amount == 25


def test_amount_to_spend__returns_initialise_price_and_step_price_sum_with_3_prices():
    amount = main.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 11, 5])
    assert amount == 22


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_price():
    amount = main.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 11, 13])
    assert amount == 0


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_prices():
    amount = main.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 8, 13, 12, 11])
    assert amount == 0
