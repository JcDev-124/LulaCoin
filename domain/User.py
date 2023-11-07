from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import rsa

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    saldo = Column(Float, default=0.0)
    public_key = Column(String)
    private_key = Column(String)

    def __init__(self, login, senha, cpf, saldo=0.0):
        self.login = login
        self.senha = senha
        self.cpf = cpf
        self.saldo = saldo
        self.generate_key_pair()

    def generate_key_pair(self):
        public_key, private_key = rsa.newkeys(512)

        public_key_pem = public_key.save_pkcs1()
        private_key_pem = private_key.save_pkcs1()

        self.public_key = public_key_pem.decode('utf-8')
        self.private_key = private_key_pem.decode('utf-8')
