def test_create_account():
    # Given

    ACCOUNT_NUMBER = 1234
    BALANCE = 5678

    # When

    account = Account(ACCOUNT_NUMBER, BALANCE)

    # Then

    assert account.account_number == ACCOUNT_NUMBER
    assert account.balance == BALANCE
