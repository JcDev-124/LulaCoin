#Validação antes de entrar no banco de dados
import hashlib
import random
import string

from domain.Block import Block

from database.Connection import DatabaseConnection


class BlockChain:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def add_block(self, data):
        return self.db_connection.block_repository.create_block(data)

    def return_blocos(self):
        return self.db_connection.block_repository.return_blocos()




    def break_hash(self, texto_original):
        def gerar_caractere_aleatorio():
            caracteres = string.ascii_letters + string.digits
            return random.choice(caracteres)

        solucao = ""
        i = 0
        for caractere_original in texto_original:
            caractere_adivinhado = gerar_caractere_aleatorio()

            while caractere_adivinhado != caractere_original:
                caractere_adivinhado = gerar_caractere_aleatorio()
                i = i + 1

            solucao += caractere_adivinhado
            print("Solucao parcial:" + solucao)
            print("           Hash:" + texto_original)
            print(i)
        return solucao



