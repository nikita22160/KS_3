import pytest

from model.transaction import Transaction


@pytest.fixture
def example_transaction():
    return Transaction(
        transaction_id=123456,
        date="2022-01-01T12:00:00.000000",
        state="EXECUTED",
        operation_amount="100.00",
        description="Test transaction",
        from_account="MasterCard1234567890",
        to_account="Счет1234567890"
    )


def test_transaction_creation(example_transaction):
    assert example_transaction.id == 123456
    assert example_transaction.state == "EXECUTED"
    assert example_transaction.operation_amount == "100.00"
    assert example_transaction.description == "Test transaction"
    assert example_transaction.from_account == "MasterCard1234567890"
    assert example_transaction.to_account == "Счет1234567890"


def test_str_method(example_transaction):
    expected_output = """
        01.01.2022 Test transaction
        Master Card 1234 56** **** 7890 -> Счет **7890
        100.00
    """.strip()

    assert str(example_transaction).strip() == expected_output


def test_str_method_opening_account():
    transaction = Transaction(
        transaction_id=123456,
        date="2022-01-01T12:00:00.000000",
        state="EXECUTED",
        operation_amount="100.00",
        description="Test transaction"
    )

    expected_output = """
        01.01.2022 Test transaction
        Открытие счета -> Открытие счета
        100.00
    """.strip()

    assert str(transaction).strip() == expected_output