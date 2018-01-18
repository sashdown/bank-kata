from bank.account import Account

def test_create_account():
    # Given

    ACCOUNT_NUMBER = 1234
    BALANCE = 5678

    # When

    account = Account(ACCOUNT_NUMBER, BALANCE)

    # Then

    assert account.account_number == ACCOUNT_NUMBER
    assert account.balance == BALANCE


def test_transfer_from_account():
    # Given
    AMOUNT = 100

    sending_account = Account(0, AMOUNT)
    receiving_account = Account(1, 0)

    # When

    sending_account.transfer(to=receiving_account, amount = AMOUNT, history=[])

    # Then

    assert  sending_account.balance == 0
    assert receiving_account.balance == AMOUNT


def test_store_transaction_history():
    # Given
    AMOUNT = 50

    sending_account = Account(0, AMOUNT)
    receiving_account = Account(1, 0)

    transaction_history = []

    # When

    sending_account.transfer(to=receiving_account, amount=AMOUNT, history=transaction_history)


    # Then

    assert len(transaction_history) == 1

    transaction = transaction_history[0]
    assert transaction.originator == sending_account
    assert transaction.destination  == receiving_account