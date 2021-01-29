import dca as dca
import pytest


def test_amount_to_spend__returns_initialise_price_when_there_is_only_one_price():
    amount = dca.Dca(dca.DcaConfiguration(price_initialisation=20, step_price=1)).compute_amount_to_spend(10, [])
    assert amount == 20


def test_amount_to_spend__returns_initialise_price_and_step_price_sum():
    amount = dca.Dca(dca.DcaConfiguration(price_initialisation=20, step_price=5)).compute_amount_to_spend(8, [10])
    assert amount == 25


def test_amount_to_spend__returns_an_amount_when_it_the_same_price_that_the_min():
    amount = dca.Dca(dca.DcaConfiguration(price_initialisation=20, step_price=5)).compute_amount_to_spend(8, [8, 8, 8])
    assert amount == 35


def test_amount_to_spend__returns_amount_when_price_only_decrease():
    amount = dca.Dca(dca.DcaConfiguration(price_initialisation=20, step_price=1)).compute_amount_to_spend(5, [10, 7])
    assert amount == 20 + 1 + 1


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_price():
    amount = dca.Dca(dca.DcaConfiguration(price_initialisation=20, step_price=1)).compute_amount_to_spend(13, [10, 11])
    assert amount == 0


def test_amount_to_spend__returns_0_if_price_is_higher_that_last_min_price():
    amount = dca.Dca(dca.DcaConfiguration(price_initialisation=20, step_price=1)).compute_amount_to_spend(11,
                                                                                                          [10, 8, 13,
                                                                                                           12])
    assert amount == 0


def test_amount_to_spend__returns_remaining_when_max_total_amount_to_spend_will_reached():
    amount = dca.Dca(dca.DcaConfiguration(price_initialisation=10, step_price=1,
                                          max_total_amount_to_spend=12)).compute_amount_to_spend(
        8, [10], total_spent=10)
    assert amount == 2


def test_amount_to_spend__raise_error_when_max_total_amount_to_spend_is_lesser_than_price_initialisation():
    with pytest.raises(Exception):
        dca.Dca(dca.DcaConfiguration(price_initialisation=10, step_price=1,
                                     max_total_amount_to_spend=8)).compute_amount_to_spend(
            8, [10])


def test_amount_to_spend__returns_additional_amount_when_there_is_new_min_price():
    amount = dca.Dca(dca.DcaConfiguration(price_initialisation=20, step_price=1)).compute_amount_to_spend(7, [10, 8, 13,
                                                                                                              12])
    assert amount == 22 + 23 + 24


def test_amount_to_spend__throws_error_when_price_initialisation_is_bigger_than_max_amount_to_spend():
    with pytest.raises(Exception):
        dca.Dca(dca.DcaConfiguration(price_initialisation=30, step_price=1,
                                     max_amount_to_spend=20)).compute_amount_to_spend(
            10, [])


def test_amount_to_spend__returns_max_amount_to_spend_when_amount_to_spent_is_bigger():
    amount = dca.Dca(
        dca.DcaConfiguration(price_initialisation=20, step_price=1, max_amount_to_spend=20)).compute_amount_to_spend(
        7, [10, 12])
    assert amount == 20


def test_amount_to_spend__max_amount_to_spent_must_not_exceeded_when_force_buy_is_set():
    amount = dca.Dca(dca.DcaConfiguration(price_initialisation=20, step_price=1, max_amount_to_spend=20,
                                          max_total_amount_to_spend=20,
                                          force_buy_under_price=20)).compute_amount_to_spend(
        4, [10, 11, 7], total_spent=30)
    assert amount == 0


def test_as_dca_configuration():
    json = '{"price_initialisation": 10, "step_price": 1}'
    dca_configuration = dca.DcaConfiguration.serialise(json)
    assert dca_configuration.price_initialisation == 10
    assert dca_configuration.step_price == 1
