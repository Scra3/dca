import dca as algo


def test_amount_to_spend__returns_initialise_price_when_there_is_only_one_price():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10])
    assert amount == 20


def test_amount_to_spend__returns_initialise_price_and_step_price_sum():
    amount = algo.Dca(price_initialisation=20, step_price=5).compute_amount_to_spend([10, 8])
    assert amount == 25


def test_amount_to_spend__returns_initialise_price_and_step_price_sum_with_3_prices():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 7, 5])
    assert amount == 22


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_price():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 11, 13])
    assert amount == 0


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_prices():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 8, 13, 12, 11])
    assert amount == 0


def test_amount_to_spend__returns_additional_amount_when_there_is_new_min_price():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 8, 13, 12, 7])
    assert amount == 22 + 23 + 24


def test_amount_to_spend__returns_additional_amount_when_there_is_new_min_price_2():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 8, 13, 12, 7, 12, 11, 6])
    assert amount == 27 + 26 + 25


def test_get_total_spent():
    amount = algo.Dca(price_initialisation=10, step_price=2).get_total_spent([10, 8, 13, 12, 8])
    assert amount == 10 + 12 + 14 + 16 + 18
