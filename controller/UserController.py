from flask import Blueprint, jsonify,request, Response
from services.UserService import UserService

user_controller = Blueprint('user', __name__)

user_service = UserService()

@user_controller.route("/users", methods=["GET"])
def get_all_users():
    users = user_service.get_all_users()
    user_list = []
    for user in users:
        user_dict = {
            'login': user.login,
            'password': user.senha,
            'cpf': user.cpf,
            'saldo': user.saldo,
            'PUBLIC_KEY': user.public_key,
            'PRIVATE_KEY': user.private_key
        }
        user_list.append(user_dict)
    return jsonify(user_list)

@user_controller.route("/users", methods=["POST"])
def post_user():
    request_data = request.get_json()
    if 'login' in request_data and 'password' in request_data and 'cpf' in request_data and 'saldo' in request_data:
        login = request_data['login']
        password = request_data['password']
        cpf = request_data['cpf']
        saldo = request_data['saldo']
        user_service.create_user(login, password, cpf, saldo)
        return jsonify({'message': 'Usuario inserido com sucesso'}), 201
    else:
        return jsonify({'message': 'Campos invalidos, verifique e tente novamente'}), 400
