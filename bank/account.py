import collections

Transaction =  collections.namedtuple('Transaction', 'originator, destination, amount')

class Account():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def transfer(self, to, amount, history):
        self.balance = self.balance - amount
        to.balance = to.balance + amount

        transaction = Transaction(originator=self, destination=to, amount=amount)
        history.append(transaction)