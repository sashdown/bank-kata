import pytest

from bank.account import Account



TRANSFER_AMOUNT = 50





def test_create_account():

    # Given

    account_number = 9876
    initial_balance = 99

    # When

    account = Account(account_number, initial_balance)

    # Then

    assert account.account_number == account_number
    assert account.balance == initial_balance


def test_transfer_from_account(payee_account, payer_account, transaction_history):

    # Given
    payer_initial_balance = payer_account.balance
    payee_initial_balance = payee_account.balance
    # When

    payer_account.transfer(payee=payee_account, amount = TRANSFER_AMOUNT, history=transaction_history)

    # Then

    assert payer_account.balance == payer_initial_balance - TRANSFER_AMOUNT
    assert payee_account.balance == payee_initial_balance + TRANSFER_AMOUNT


def test_store_transaction_history(payee_account, payer_account, transaction_history):

    # When

    payer_account.transfer(payee=payee_account, amount=TRANSFER_AMOUNT, history=transaction_history)

    # Then

    assert len(transaction_history) == 1

    transaction = transaction_history[0]
    assert transaction.payer == payer_account
    assert transaction.payee == payee_account
    assert transaction.amount == TRANSFER_AMOUNT
