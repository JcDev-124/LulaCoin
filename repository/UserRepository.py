from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from domain.User import User

class UserRepository:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_user(self, login, senha, cpf, saldo=0.0):
        session = self.Session()
        user = User(login=login, senha=senha, cpf=cpf, saldo=saldo)
        session.add(user)
        session.commit()
        session.close()

    def get_user_by_login(self, login):
        session = self.Session()
        user = session.query(User).filter_by(login=login).first()
        session.close()
        return user

    def get_user_by_key(self, public_key):
        session = self.Session()
        user = session.query(User).filter_by(public_key=public_key).first()
        session.close()
        return user

    def get_user_by_key_private(self, private_key):
        session = self.Session()
        user = session.query(User).filter_by(private_key=private_key).first()
        session.close()
        return user
    def get_all_users(self):
        session = self.Session()
        users = session.query(User).all()
        session.close()
        return users

    def update_user_balance_destinatario(self, public_key, new_balance):
        session = self.Session()
        user = session.query(User).filter_by(public_key=public_key).first()
        if user:
            user.saldo = new_balance + user.saldo
            session.commit()

        session.close()

    def update_user_balance_remetente(self, private_key, new_balance):
        session = self.Session()
        user = session.query(User).filter_by(private_key=private_key).first()
        if user:
            user.saldo = user.saldo - new_balance
            session.commit()

        session.close()