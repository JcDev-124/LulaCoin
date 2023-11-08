#Criar uma transação de bitcoins
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import rsa

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions_pending'
    id = Column(Integer, primary_key=True)
    public_key = Column(String, nullable=False)
    private_key = Column(String, nullable=False)
    taxa = Column(Float, default=0.0)
    valor = Column(Float, default=0.0)

    def __init__(self, public_key, private_key, taxa, valor):
        self.public_key = public_key
        self.private_key = private_key
        self.taxa = taxa
        self.valor = valor

