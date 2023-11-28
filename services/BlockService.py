#Validação antes de entrar no banco de dados
import hashlib

from database.Connection import DatabaseConnection


class BlockChain:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def add_block(self, data):
        return self.db_connection.block_repository.create_block(data)

    def return_blocos(self):
        return self.db_connection.block_repository.return_blocos()

    @classmethod
    def break_hash(cls, target_hash):
        nonce = 0

        while True:
            candidate_hash = hashlib.sha256(str(nonce).encode()).hexdigest()

            if candidate_hash == target_hash:
                return nonce
            print("Numero de nonces", nonce)
            print("Canditado", candidate_hash)
            nonce += 1

