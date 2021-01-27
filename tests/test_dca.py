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


def test_amount_to_spend__returns_an_amount_when_it_the_same_price_that_the_min():
    amount = algo.Dca(price_initialisation=20, step_price=5).compute_amount_to_spend([8, 8, 8, 8])
    assert amount == 35


def test_amount_to_spend__returns_amount_when_price_only_decrease():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 7, 5])
    assert amount == 20 + 1 + 1


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_price():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 11, 13])
    assert amount == 0


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_min_price():
    amount = algo.Dca(price_initialisation=20, step_price=1).compute_amount_to_spend([10, 8, 13, 12, 11])
    assert amount == 0


def test_amount_to_spend__returns_remaining_when_max_total_amount_to_spend_will_reached():
    amount = algo.Dca(price_initialisation=10, step_price=1,
                      max_total_amount_to_spend=12).compute_amount_to_spend(
        [10, 8], total_spent=10)
    assert amount == 2


def test_amount_to_spend__raise_error_when_max_total_amount_to_spend_is_lesser_than_price_initialisation():
    with pytest.raises(Exception):
        algo.Dca(price_initialisation=10, step_price=1, max_total_amount_to_spend=8).compute_amount_to_spend(
            [10, 8])


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


def test_amount_to_spend__max_amount_to_spent_must_not_exceeded_when_force_buy_is_set():
    amount = algo.Dca(price_initialisation=20, step_price=1, max_amount_to_spend=20,
                      max_total_amount_to_spend=20,
                      force_buy_under_price=20).compute_amount_to_spend(
        [10, 11, 7, 4], total_spent=30)
    assert amount == 0


def test_get_average_price():
    price = algo.Dca.get_average_price(total_spent=10, balance=5)
    assert price == 10 / 5


def test_get_with_real_history():
    history = [price[1] for price in get_only_tuesday_days()]
    dca = algo.Dca(price_initialisation=20, step_price=2,
                   force_buy_under_price=3500)
    balance = 0
    total_spent = 0
    for index, _ in enumerate(history):
        amount = dca.compute_amount_to_spend(history[0:index + 1], total_spent)
        total_spent += amount
        balance += amount / history[index]

    average = algo.Dca.get_average_price(total_spent=total_spent, balance=balance)
    assert average == 3716.647913018985
    assert total_spent == 3944.0
    assert balance == 1.0611712737665107
