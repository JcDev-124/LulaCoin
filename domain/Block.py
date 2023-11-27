# Entidade Blocos

from sqlalchemy import Column, Integer, String, DateTime, Sequence
from sqlalchemy.ext.declarative import declarative_base
import hashlib
import datetime

Base = declarative_base()

class Block(Base):
    __tablename__ = 'Blocks' #Nome da tebela no banco de dados
    id = Column(Integer, Sequence('block_id_seq'), primary_key=True)
    timestamp = Column(DateTime) #Data e hora de quando o bloco foi validado
    data = Column(String) #Lista de Transações
    previous_hash = Column(String) #Hash do bloco anterior
    hash = Column(String) #Hash do bloco atual

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        
    #Função para o calculo do hash
    def calculate_hash(self): 
        sha = hashlib.sha256()
        data_to_hash = f"{self.timestamp}{self.data}{self.previous_hash}".encode('utf-8')
        sha.update(data_to_hash)
        return sha.hexdigest()
