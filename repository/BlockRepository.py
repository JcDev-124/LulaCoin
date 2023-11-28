#Trato com o banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.Block import Block

class BlockRepository:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_block(self, data):
        session = self.Session()
        last_block = session.query(Block).order_by(Block.id.desc()).first()

        if last_block:
            previous_hash = last_block.hash
            new_block = Block(data, previous_hash)
            session.add(new_block)
            session.commit()
            created_block_data = {
                'hash': new_block.hash
            }
            session.close()
            return created_block_data
        else:
            new_block = Block(data, "0")
            session.add(new_block)
            session.commit()
            created_block_data = {
                'hash': new_block.hash
            }
            session.close()
            return created_block_data


    def return_blocos(self):
        session = self.Session()
        blocos = session.query(Block).all()
        session.close()
        return blocos