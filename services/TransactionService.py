

from database.Connection import DatabaseConnection
class TransactionService:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def create_transaction(self, public_key, private_key, taxa, valor):
        self.db_connection.transaction_repository.create_transaction(public_key,private_key,taxa,valor)
    def get_all(self):
        return self.db_connection.transaction_repository.return_transactions()
