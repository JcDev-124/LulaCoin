#Validação antes de entrar no banco de dados
from database.Connection import DatabaseConnection

class UserService:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def create_user(self, login, senha, cpf, saldo=0.0):
        self.db_connection.user_repository.create_user(login, senha, cpf, saldo)

    def get_all_users(self):
        return self.db_connection.user_repository.get_all_users()

    def get_user_login(self, login):
        return self.db_connection.user_repository.get_user_by_login(login)
    def get_user_key(self, public_key):
        return self.db_connection.user_repository.get_user_by_key(public_key)
    def get_user_key_private(self, private_key):
        return self.db_connection.user_repository.get_user_by_key_private(private_key)
    def update_saldo_remetente(self, private_key, valor):
        self.db_connection.user_repository.update_user_balance_remetente(private_key,valor)
    def update_saldo_destinario(self, public_key, valor):
        self.db_connection.user_repository.update_user_balance_destinatario(public_key,valor)


