import dca as algo
import datetime as dt
import data as data
import pytest


def get_only_tuesday_days():
    filtered_prices = []
    for price in data.prices:
        timestamp = price[0] / 1000
        date = dt.datetime.fromtimestamp(timestamp)
        if date.weekday() == 2:
            filtered_prices.append(price)

    return filtered_prices


def test_amount_to_spend__returns_initialise_price_when_there_is_only_one_price():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10])
    assert amount == 20


def test_amount_to_spend__returns_initialise_price_and_step_price_sum():
    amount = algo.Dca(price_initialisation=20, step_price=5).compute_amount_to_spend([10, 8])
    assert amount == 25


def test_amount_to_spend__returns_amount_when_price_only_decrease():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 7, 5])
    assert amount == 20 + 1 + 1


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_price():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 11, 13])
    assert amount == 0


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_min_price():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 8, 13, 12, 11])
    assert amount == 0


def test_amount_to_spend__returns_additional_amount_when_there_is_new_min_price():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 8, 13, 12, 7])
    assert amount == 22 + 23 + 24


def test_amount_to_spend__throws_error_when_price_initialisation_is_bigger_than_max_amount_to_spend():
    with pytest.raises(Exception):
        algo.Dca(price_initialisation=30, step_price=1, max_amount_to_spend=20).compute_amount_to_spend(
            [10])


def test_amount_to_spend__returns_max_amount_to_spend_when_amount_to_spent_is_bigger():
    amount = algo.Dca(price_initialisation=20, step_price=1, max_amount_to_spend=20).compute_amount_to_spend(
        [10, 12, 7])
    assert amount == 20


def test_get_total_spent():
    amount = algo.Dca(price_initialisation=10, step_price=2).get_total_spent([10, 8, 13, 12, 8])
    assert amount == 10 + 12 + 14 + 16 + 18


def test_get_balance():
    amount = algo.Dca(price_initialisation=10, step_price=2).get_balance([10, 8, 13, 12, 8])
    expected_result = 10 / 10 + 12 / 8 + (14 + 16 + 18) / 8
    assert amount == expected_result


def test_get_average_amount():
    amount = algo.Dca(price_initialisation=10, step_price=2).get_average_amount([10, 8, 13, 12, 8])
    assert amount == 8.235294117647058


def test_get_average_amount_with_real_prices():
    history = [price[1] for price in get_only_tuesday_days()]
    amount = algo.Dca(price_initialisation=20, step_price=2, force_buy_under_price=3500).get_average_amount(history)
    assert amount == 3716.647913018985


def test_get_total_spent_with_real_prices():
    history = [price[1] for price in get_only_tuesday_days()]
    amount = algo.Dca(price_initialisation=24, step_price=0.50, force_buy_under_price=3500).get_total_spent(history)
    assert amount == 2012.0


def test_get_balance_with_real_prices():
    history = [price[1] for price in get_only_tuesday_days()]
    amount = algo.Dca(price_initialisation=24, step_price=0.50, force_buy_under_price=3500).get_balance(history)
    assert amount == 0.5208075112693835
