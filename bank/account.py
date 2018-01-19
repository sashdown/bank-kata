import collections

Transaction = collections.namedtuple('Transaction', 'payer, payee, amount')


class Account():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def transfer(self, payee, amount, history):
        self.balance = self.balance - amount
        payee.balance = payee.balance + amount

        transaction = Transaction(payer=self, payee=payee, amount=amount)
        history.append(transaction)