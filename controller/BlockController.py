

from flask import Blueprint, jsonify,request
from services.BlockService import BlockChain
from services.UserService import UserService
import json

block_controller = Blueprint('block', __name__)

block_service = BlockChain()
user_service = UserService()
@block_controller.route("/block", methods=["POST"])
def post_block():
    if request.is_json:
        data = request.get_json()
        if isinstance(data, list) and data:
            processed_data = []
            for obj in data:
                processed_data.append(obj)
                public_key = obj['public_key']
                private_key = obj['private_key']
                taxa = obj['taxa']
                valor = obj['valor']
                user_service.update_saldo_remetente(private_key, valor)
                user_service.update_saldo_destinario(public_key, valor)
            objeto_string = json.dumps(data)
            block_service.add_block(objeto_string)
            return jsonify({'message': 'Bloco validado'}), 201
        else:
            return jsonify({'error': 'Formato inválido ou lista vazia'}), 400
    else:
        return jsonify({'error': 'Requisição não contém dados JSON'}), 400
@block_controller.route("/block", methods=["GET"])
def get_blocos():
    blocos = block_service.return_blocos()
    blocos_list = []
    for block in blocos:
        blocos_dict = {
            'posicao': block.posicao,
            'time': block.timestamp,
            'dados': block.data,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        }
        blocos_list.append(blocos_dict)
    return jsonify(blocos_list), 200