class TransactionHistory(list):
    def find_transactions(self, **kwargs):
        payer = kwargs.get("payer", None)
        payee = kwargs.get("payee", None)

        if payer:
            return [transaction for transaction in self if transaction.payer == payer]

        if payee:
            return [transaction for transaction in self if transaction.payee == payee]