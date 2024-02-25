import pytest

from model.transaction import Transaction


@pytest.fixture
def example_transaction():
    return Transaction(
        transaction_id=895315941,
        date="2018-08-19T04:27:37.904916",
        state="EXECUTED",
        operation_amount="56883.54 USD",
        description="Перевод с карты на карту",
        from_account="Visa Classic 6831982476737658",
        to_account="Visa Platinum 8990922113665229"
    )


def test_str_method(example_transaction):
    expected_output = """
        19.08.2018 Перевод с карты на карту
        Visa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229
        56883.54 USD
    """.strip()

    assert str(example_transaction).strip() == expected_output