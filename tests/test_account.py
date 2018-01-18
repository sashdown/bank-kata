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

    sending_account =  Account(0, AMOUNT)
    receiving_account = Account(1, 0)

    # When

    sending_account.transfer(to=receiving_account, amount = AMOUNT)

    # Then

    assert  sending_account.balance == 0
    assert receiving_account.balance == AMOUNT
