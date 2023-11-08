from flask import Blueprint, jsonify,request, Response
from services import TransactionService


transaction_controller = Blueprint('transaction', __name__)

@transaction_controller.route("/transaction", methods = ["POST"])
def created_transaction():
    request_data = request.get_json()
    if 'public_key' not in request_data or 'private_key' not in request_data or 'valor' not in request_data:
        return jsonify({'message': 'Campos inválidos, verifique e tente novamente'}), 400


