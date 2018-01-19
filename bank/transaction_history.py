class TransactionHistory:

    def __init__(self):
        self.transactions = []

    def record(self, transaction):
        self.transactions.append(transaction)

    def find_transactions(self, **kwargs):
        """
        Return transactions with accounts matching (optional) supplied payer or payee accounts
        If both payee and payer arguments are supplied, only return transactions from payer to payee
        If no arguments are supplied, return all transactions
        """

        payer = kwargs.get("payer", None)
        payee = kwargs.get("payee", None)

        candidate_transactions = [transaction for transaction in self.transactions]

        if payer:
            candidate_transactions = [transaction for transaction in candidate_transactions if
                                      transaction.payer == payer]

        if payee:
            candidate_transactions = [transaction for transaction in candidate_transactions if
                                      transaction.payee == payee]

        return candidate_transactions
