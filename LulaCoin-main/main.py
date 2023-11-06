from domain.Block import Block
from services.BlockService import BlockChain

# Criando uma instância da blockchain
blockchain = BlockChain()

# Adicionando blocos
blockchain.add_block()
blockchain.add_block()
blockchain.add_block()

# Impressão dos blocos
blockchain.print_block()

# Verificando a validade da blockchain
if blockchain.is_valid():
    print("Blockchain válida")
else:
    print("Blockchain inválida")