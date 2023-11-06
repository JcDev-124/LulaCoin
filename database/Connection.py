
from repository.UserRepository import UserRepository

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.initialize_connection()
        return cls._instance

    def initialize_connection(self):


        with open('C:\\Users\\Julio\\PycharmProjects\\LulaCoin\\db_config.txt', 'r') as file:
            db_url = file.read().strip()
            self.user_repository = UserRepository(db_url)