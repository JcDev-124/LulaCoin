from sqlalchemy import Column, Integer, String, DateTime, Sequence
from sqlalchemy.ext.declarative import declarative_base
import hashlib
import datetime

Base = declarative_base()

class Block(Base):
    __tablename__ = 'Blocks'

    id = Column(Integer, Sequence('block_id_seq'), primary_key=True)
    posicao = Column(Integer, Sequence('posicao_seq'), server_default="1", nullable=False)
    timestamp = Column(DateTime)
    data = Column(String)
    previous_hash = Column(String)
    hash = Column(String)

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        data_to_hash = f"{self.posicao}{self.timestamp}{self.data}{self.previous_hash}".encode('utf-8')
        sha.update(data_to_hash)
        return sha.hexdigest()
