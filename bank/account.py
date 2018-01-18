class Account():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def transfer(self, to, amount):
        self.balance = self.balance - amount
        to.balance = to.balance + amount