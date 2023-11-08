import self

from database.Connection import DatabaseConnection
class TransactionService:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def create_transaction(public_key, private_key, taxa, valor):
        self.db_connection.TransactionRepository.create_transaction(public_key,private_key,taxa,valor)
