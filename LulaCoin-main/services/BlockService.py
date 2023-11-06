from datetime import datetime
from domain.Block import Block

class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0", 0)  # Assumindo que o block_count inicial é 0

    def add_block(self):
        new_block_description = input("Descreva a transferência: ")
        block_count = len(self.chain)  # Atualizando o contador de blocos na cadeia
        previous_block = self.chain[block_count - 1]
        new_block_hash = previous_block.hash
        self.chain.append(Block(new_block_description, new_block_hash, block_count))

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def print_block(self):
        for block in self.chain:
            print(f'Hash Atual: {block.hash}')
            print(f'Hash anterior: {block.previous_hash}')
            print(20*'----')