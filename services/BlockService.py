#Validação antes de entrar no banco de dados
from database.Connection import DatabaseConnection


class BlockChain:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def add_block(self, data):
        self.db_connection.block_repository.create_block(data)

    def return_blocos(self):
        return self.db_connection.block_repository.return_blocos()

