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
    def return_transactions(self):
        session = self.Session()
        transactions = session.query(Transaction).all()
        session.close()
        return transactions

    def delete_transactions(self, data):
        session = self.Session()

        try:
            transactions_to_delete = data.get("transacoes", [])

            for transaction_data in transactions_to_delete:
                id = transaction_data.get("cod")

                # Exclui todas as transações com o código fornecido
                transactions = session.query(Transaction).filter_by(id=id).all()
                for transaction in transactions:
                    session.delete(transaction)

            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


