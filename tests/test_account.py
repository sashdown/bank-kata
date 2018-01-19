from bank.account import Account

PAYEE_ACCOUNT_NUMBER = 1234
PAYER_ACCOUNT_NUMBER = 5678

TRANSFER_AMOUNT = 100

def test_create_account():
    # Given

    BALANCE = 5678

    # When

    account = Account(PAYER_ACCOUNT_NUMBER, BALANCE)

    # Then

    assert account.account_number == PAYER_ACCOUNT_NUMBER
    assert account.balance == BALANCE


def test_transfer_from_account():
    # Given


    sending_account = Account(PAYER_ACCOUNT_NUMBER, TRANSFER_AMOUNT)
    receiving_account = Account(PAYEE_ACCOUNT_NUMBER, 0)

    # When

    sending_account.transfer(payee=receiving_account, amount = TRANSFER_AMOUNT, history=[])

    # Then

    assert  sending_account.balance == 0
    assert receiving_account.balance == TRANSFER_AMOUNT


def test_store_transaction_history():
    # Given

    sending_account = Account(PAYER_ACCOUNT_NUMBER, TRANSFER_AMOUNT)
    receiving_account = Account(PAYEE_ACCOUNT_NUMBER, 0)

    transaction_history = []

    # When

    sending_account.transfer(payee=receiving_account, amount=TRANSFER_AMOUNT, history=transaction_history)


    # Then

    assert len(transaction_history) == 1

    transaction = transaction_history[0]
    assert transaction.payer == sending_account
    assert transaction.payee == receiving_account