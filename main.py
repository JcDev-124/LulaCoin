from datetime import datetime

from domain.block import Block

from domain.blockchain import BlockChain

my_blockchain = BlockChain()

compra1 = {
    'item': 'Ford',
    'valor': 100,
    'comprador': 'eu',
    'vendedor': 'eutambem'
}

compra2 = {
    'item': 'Mustang',
    'valor': 100,
    'comprador': 'eu',
    'vendedor': 'eutambem'
}

my_blockchain.add_block(Block(1, datetime.now(), compra1, my_blockchain.chain[-1].hash))
my_blockchain.add_block(Block(2, datetime.now(), compra2, my_blockchain.chain[-1].hash))

print(f'Essa blockchain esta valida?  {str(my_blockchain.is_valid())}')

my_blockchain.print_block()
