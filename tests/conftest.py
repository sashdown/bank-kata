import pytest

from bank.account import Account
from bank.transaction_history import TransactionHistory

PAYEE_ACCOUNT_NUMBER = 1234
PAYER_ACCOUNT_NUMBER = 5678

INITIAL_BALANCE = 100

@pytest.fixture
def payee_account():
    return Account(PAYEE_ACCOUNT_NUMBER, 0)


@pytest.fixture
def payer_account():
    return Account(PAYER_ACCOUNT_NUMBER, INITIAL_BALANCE)

@pytest.fixture
def transaction_history(scope="function"):
    return TransactionHistory()