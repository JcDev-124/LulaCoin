from flask import Blueprint, jsonify,request
from services.BlockService import BlockChain
from services.UserService import UserService
from services.TransactionService import TransactionService
import json

block_controller = Blueprint('block', __name__)

block_service = BlockChain()
user_service = UserService()
transaction_service = TransactionService()


@block_controller.route("/block", methods=["POST"])
def post_block():
    if request.is_json:
        data = request.get_json()
        objeto_string = json.dumps(data)
        #hash = block_service.add_block(objeto_string).get('hash')
        #print(hash)
        #nonce_found = block_service.break_hash(hash)
        #print("Nonce encontrado: ", nonce_found)
        transaction_service.delete_transcactions(data)

        key_minerador = data.get("key_minerador")
        processed_data = {"transacoes": []}
        valor = 0

        if isinstance(data.get("transacoes"), list):
            for obj in data["transacoes"]:
                processed_data["transacoes"].append(obj)
                public_key = obj.get('public_key')
                private_key = obj.get('private_key')
                taxa = obj.get('taxa')
                valor += obj.get('valor')
                user_service.update_saldo_remetente(private_key, valor)
                user_service.update_saldo_destinario(public_key, valor)

        user_service.update_saldo_destinario(key_minerador, valor * taxa)

        return jsonify({'message': 'Bloco validado'}), 201
    else:
        return jsonify({'error': 'Requisição não contém dados JSON'}), 400
@block_controller.route("/block", methods=["GET"])
def get_blocos():
    blocos = block_service.return_blocos()
    blocos_list = []
    for block in blocos:
        try:
            dados_json = json.loads(block.data)
        except json.JSONDecodeError:
            dados_json = block.data

        blocos_dict = {
            'time': block.timestamp,
            'dados': dados_json,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        }
        blocos_list.append(blocos_dict)
    return jsonify(blocos_list), 200