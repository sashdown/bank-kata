from bank.account import Transaction


def test_find_single_transaction_in_history(transaction_history, payee_account, payer_account):

    # Given
    AMOUNT = 100
    transaction = Transaction(payee=payee_account, payer=payer_account, amount = AMOUNT)

    # When
    matching_transactions = transaction_history.find_transactions(payee_account == payee_account)

    # Then

    assert len (matching_transactions) == 0
    assert matching_transactions[0] == transaction