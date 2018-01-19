from bank.account import Transaction


def test_find_single_transaction_in_history(transaction_history, payee_account, payer_account):

    # Given
    AMOUNT = 100
    transaction = Transaction(payee=payee_account, payer=payer_account, amount = AMOUNT)
    transaction_history.append(transaction)
    # When
    matching_transactions = transaction_history.find_transactions(payer=payer_account)

    # Then

    assert len (matching_transactions) == 1
    assert matching_transactions[0] == transaction

def test_find_single_transaction_in_history_containing_other_account_transactions(transaction_history,
                                                                      payee_account,
                                                                      payer_account,
                                                                      alternative_payer_account):

    # Given

    target_transaction = Transaction(payee=payee_account, payer=payer_account, amount = 100 )
    other_transaction = Transaction(payee=payee_account, payer=alternative_payer_account, amount= 55)

    transaction_history.append(other_transaction)
    transaction_history.append(target_transaction)

    # When
    matching_transactions = transaction_history.find_transactions(payer = payer_account)

    # Then

    assert len (matching_transactions) == 1
    assert matching_transactions[0] == target_transaction