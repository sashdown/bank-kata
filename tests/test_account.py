import pytest

from bank.account import Account
from bank.transaction_history import TransactionHistory

PAYEE_ACCOUNT_NUMBER = 1234
PAYER_ACCOUNT_NUMBER = 5678

TRANSFER_AMOUNT = 50
INITIAL_BALANCE = 100

@pytest.fixture
def payee_account():
    return Account(PAYEE_ACCOUNT_NUMBER, 0)

@pytest.fixture
def payer_account():
    return Account(PAYER_ACCOUNT_NUMBER, INITIAL_BALANCE)

@pytest.fixture
def transaction_history():
    return TransactionHistory()

def test_create_account():

    # When

    account = Account(PAYER_ACCOUNT_NUMBER, INITIAL_BALANCE)

    # Then

    assert account.account_number == PAYER_ACCOUNT_NUMBER
    assert account.balance == INITIAL_BALANCE


def test_transfer_from_account(payee_account, payer_account, transaction_history):

    # When

    payer_account.transfer(payee=payee_account, amount = TRANSFER_AMOUNT, history=transaction_history)

    # Then

    assert payer_account.balance == INITIAL_BALANCE - TRANSFER_AMOUNT
    assert payee_account.balance == TRANSFER_AMOUNT


def test_store_transaction_history(payee_account, payer_account, transaction_history):

    # When

    payer_account.transfer(payee=payee_account, amount=TRANSFER_AMOUNT, history=transaction_history)

    # Then

    assert len(transaction_history) == 1

    transaction = transaction_history[0]
    assert transaction.payer == payer_account
    assert transaction.payee == payee_account
    assert transaction.amount == TRANSFER_AMOUNT
