import portfolio as model
import pytest


@pytest.fixture
def drop_databases_after_test():
    yield
    model.Portfolio().drop_db()


def test_get_total_spent_when_adding_on_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(10)

    total_spent = model.Portfolio().get_total_spend()

    assert total_spent == 10


def test_get_total_spent_when_adding_several_amount_spent(drop_databases_after_test):
    model.Portfolio().save_spent(10)
    model.Portfolio().save_spent(24.5)

    total_spent = model.Portfolio().get_total_spend()

    assert total_spent == 10 + 24.5
