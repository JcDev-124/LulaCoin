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

    def get_user_by_cpf(self, cpf):
        session = self.Session()
        user = session.query(User).filter_by(cpf=cpf).first()
        session.close()
        return user

    def update_user_saldo(self, login, new_saldo):
        session = self.Session()
        user = session.query(User).filter_by(login=login).first()
        if user:
            user.saldo = new_saldo
            session.commit()
        session.close()
