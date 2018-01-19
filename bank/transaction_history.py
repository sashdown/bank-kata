class TransactionHistory(list):
    def find_transactions(self, payer):
        return [self[0]]