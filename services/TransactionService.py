

from database.Connection import DatabaseConnection
from services.UserService import UserService

user_service = UserService()
class TransactionService:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def create_transaction(self, public_key, private_key, taxa, valor):
        destinatario = user_service.get_user_key(public_key)
        remetente = user_service.get_user_key_private(private_key)
        if destinatario is None:
            return 1
        if remetente is None:
            return 2
        if destinatario.private_key == remetente.private_key:
            return 3
        if remetente.saldo < valor:
            return 4
        self.db_connection.transaction_repository.create_transaction(public_key, private_key, taxa, valor)
        return 5

    def get_all(self):
        return self.db_connection.transaction_repository.return_transactions()
    def delete_transcactions(self, data):
        self.db_connection.transaction_repository.delete_transactions(data)