from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.Transaction import Transaction
class TransactionRepository:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_transaction(self, public_key, private_key, taxa, valor):
        session = self.Session()
        transaction = Transaction(public_key,private_key,taxa,valor)
        session.add(transaction)
        session.commit()
        session.close()