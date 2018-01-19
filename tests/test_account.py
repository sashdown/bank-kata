from bank.account import Account

PAYEE_ACCOUNT_NUMBER = 1234
PAYER_ACCOUNT_NUMBER = 5678

TRANSFER_AMOUNT = 50
INITIAL_BALANCE = 100


def test_create_account():

    # When

    account = Account(PAYER_ACCOUNT_NUMBER, INITIAL_BALANCE)

    # Then

    assert account.account_number == PAYER_ACCOUNT_NUMBER
    assert account.balance == INITIAL_BALANCE


def test_transfer_from_account():
    # Given

    sending_account = Account(PAYER_ACCOUNT_NUMBER, INITIAL_BALANCE)
    receiving_account = Account(PAYEE_ACCOUNT_NUMBER, 0)

    # When

    sending_account.transfer(payee=receiving_account, amount = TRANSFER_AMOUNT, history=[])

    # Then

    assert sending_account.balance == INITIAL_BALANCE - TRANSFER_AMOUNT
    assert receiving_account.balance == TRANSFER_AMOUNT


def test_store_transaction_history():
    # Given

    sending_account = Account(PAYER_ACCOUNT_NUMBER, INITIAL_BALANCE)
    receiving_account = Account(PAYEE_ACCOUNT_NUMBER, 0)

    transaction_history = []

    # When

    sending_account.transfer(payee=receiving_account, amount=TRANSFER_AMOUNT, history=transaction_history)

    # Then

    assert len(transaction_history) == 1

    transaction = transaction_history[0]
    assert transaction.payer == sending_account
    assert transaction.payee == receiving_account
    assert transaction.amount == TRANSFER_AMOUNT
