from bank.account import Transaction


def test_find_single_transaction_in_history_by_payer(transaction_history, payee_account, payer_account):
    # Given

    transaction = Transaction(payee=payee_account, payer=payer_account, amount=100)
    transaction_history.record(transaction=transaction)

    # When
    matching_transactions = transaction_history.find_transactions(payer=payer_account)

    # Then

    assert [transaction] == matching_transactions


def test_find_multiple_transactions_in_history_by_payer(transaction_history, payee_account, payer_account):
    # Given

    first_transaction = Transaction(payee=payee_account, payer=payer_account, amount=1)
    transaction_history.record(transaction=first_transaction)

    second_transaction = Transaction(payee=payee_account, payer=payer_account, amount=2)
    transaction_history.record(transaction=second_transaction)

    # When
    matching_transactions = transaction_history.find_transactions(payer=payer_account)

    # Then

    assert 2 == len(matching_transactions)
    assert first_transaction in matching_transactions
    assert second_transaction in matching_transactions


def test_find_single_transaction_in_history_by_payer_containing_other_account_transactions(transaction_history,
                                                                                           payee_account,
                                                                                           payer_account,
                                                                                           alternative_account):
    # Given

    target_transaction = Transaction(payee=payee_account, payer=payer_account, amount=100)
    other_transaction = Transaction(payee=payee_account, payer=alternative_account, amount=55)

    transaction_history.record(transaction=other_transaction)
    transaction_history.record(transaction=target_transaction)

    # When
    matching_transactions = transaction_history.find_transactions(payer=payer_account)

    # Then

    assert [target_transaction] == matching_transactions


def test_find_single_transaction_in_history_by_payee(transaction_history, payee_account, payer_account):
    # Given

    transaction = Transaction(payee=payee_account, payer=payer_account, amount=100)
    transaction_history.record(transaction=transaction)

    # When
    matching_transactions = transaction_history.find_transactions(payee=payee_account)

    # Then

    assert [transaction] == matching_transactions


def test_find_single_transaction_in_history_by_payee_containing_other_account_transactions(transaction_history,
                                                                                           payee_account,
                                                                                           payer_account,
                                                                                           alternative_account):
    # Given

    target_transaction = Transaction(payee=payee_account, payer=payer_account, amount=100)
    other_transaction = Transaction(payee=alternative_account, payer=payer_account, amount=55)

    transaction_history.record(transaction=other_transaction)
    transaction_history.record(transaction=target_transaction)

    # When
    matching_transactions = transaction_history.find_transactions(payee=payee_account)

    # Then

    assert [target_transaction] == matching_transactions


def test_find_multiple_transactions_in_history_by_payee(transaction_history, payee_account, alternative_account):
    # Given

    first_transaction = Transaction(payee=payee_account, payer=alternative_account, amount=1)
    transaction_history.record(transaction=first_transaction)

    second_transaction = Transaction(payee=payee_account, payer=alternative_account, amount=2)
    transaction_history.record(transaction=second_transaction)

    # When
    matching_transactions = transaction_history.find_transactions(payee=payee_account)

    # Then

    assert 2 == len(matching_transactions)
    assert first_transaction in matching_transactions
    assert second_transaction in matching_transactions


def test_find_transaction_only_matching_payer_and_payee_when_both_supplied(
        transaction_history, payee_account, alternative_account, payer_account):
    # Given

    target_transaction = Transaction(payee=payee_account, payer=payer_account, amount=1)

    transaction_history.record(transaction=target_transaction)

    transaction_history.record(transaction=Transaction(payee=payee_account, payer=alternative_account, amount=2))
    transaction_history.record(transaction=Transaction(payee=alternative_account, payer=payer_account, amount=3))

    # When
    matching_transactions = transaction_history.find_transactions(payer=payer_account, payee=payee_account)

    # Then

    assert [target_transaction] == matching_transactions
