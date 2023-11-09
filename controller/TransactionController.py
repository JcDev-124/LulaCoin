from flask import Blueprint, jsonify,request, Response
from services.TransactionService import TransactionService

transaction_controller = Blueprint('transaction', __name__)

transaction_service = TransactionService()

@transaction_controller.route("/transaction", methods = ["POST"])
def created_transaction():
    request_data = request.get_json()
    if 'public_key' not in request_data or 'private_key' not in request_data or 'valor' not in request_data:
        return jsonify({'message': 'Campos inválidos, verifique e tente novamente'}), 400
    private_key = request_data['private_key']
    public_key = request_data['public_key']
    taxa = request_data.get('taxa', 0.0)
    valor = request_data['valor']
    transaction_service.create_transaction(public_key,private_key,taxa,valor)
    return jsonify({'message': 'transacao criada'}), 200




