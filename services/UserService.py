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



