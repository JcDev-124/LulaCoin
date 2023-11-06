#Imports
import datetime
import hashlib

#Variáveis Globais e Constantes
block_count = 0

#Classes
class Block:
    #Construtor
    def __init__(self, description, previous_hash, block_count):
        self.index = block_count
        block_count += 1
        self.time = datetime.datetime.now()
        self.description = description
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    #Método para calculo do Hash
    def calculate_hash(self):
        data = str(self.index) + str(self.time) + str(self.description) + str(self.previous_hash)
        return hashlib.sha256(data.encode()).hexdigest()

#Funções
def create_genesis_block():
    #Define o primeiro bloco da cadeia
    return Block("Genesis Block", "0", block_count)  

def add_block():
    new_block_descripton = input("Descreva a transferência: ")
    previous_block = blockchain[block_count - 1]
    new_block_hash = previous_block.hash
    blockchain.append(Block(new_block_descripton, new_block_hash, block_count))

#Main
blockchain = [create_genesis_block()]
add_block()
add_block()
add_block()

# Printing the blocks
for block in blockchain:
    print(f"Block #{block.index} - Hash: {block.hash[0:5]} - Previous Hash: {block.previous_hash[0:5]}")