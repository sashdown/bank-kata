class TransactionHistory(list):
    def find_transactions(self, payer):
        return [transaction for transaction in self if transaction.payer == payer ]