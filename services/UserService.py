from database.Connection import DatabaseConnection
class UserService:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def create_user(self, login, senha, cpf, saldo=0.0):
        self.db_connection.user_repository.create_user(login, senha, cpf, saldo)


