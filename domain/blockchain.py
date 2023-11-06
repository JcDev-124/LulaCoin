from datetime import datetime

from domain.block import Block

class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.now(), 'Genesis block', '0')

    def add_block(self, newBlock):
        newBlock.previous_hash = self.chain[-1].hash
        newBlock.hash = newBlock.calculate_hash()
        self.chain.append(newBlock)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if(current_block.hash != current_block.calculate_hash()):
                return False
            if(current_block.previous_hash != previous_block.hash):
                return False

            return True

    def print_block(self):
        for block in self.chain:
            print(f'Block: {block.index}')
            print(f'TimeStamp: {block.timestamp}')
            print(f'Data: {block.data}')
            print(f'Hash Atual: {block.hash}')
            print(f'Hash anterior: {block.previous_hash}')
            print(20*'----')