from datetime import datetime

from domain.Block import Block

from services.BlockService import BlockChain
from services.UserService import UserService
my_blockchain = BlockChain()

compra1 = {
    'Pagante': 'Julio',
    'Recebedor': 'Kevin',
    'Valor': 1,
}

dificuldade = int(input("Digite a dificuldade: "))
for i in range(dificuldade):
    my_blockchain.add_block(Block(i + 1, datetime.now(), compra1, my_blockchain.chain[-1].hash))


my_blockchain.print_block()

print(f'Essa blockchain esta valida?  {str(my_blockchain.is_valid())}')

if __name__ == "__main__":
    user_service = UserService()
    user_service.create_user('usuario', 'senhaa', '1234', '1000')