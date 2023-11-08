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

    # Verifique os campos obrigatórios
    if 'login' not in request_data or 'password' not in request_data:
        return jsonify({'message': 'Campos inválidos, verifique e tente novamente'}), 400

    login = request_data['login']
    password = request_data['password']

    user = user_service.get_user_login(login)

    if user is None:
        return jsonify({'message': 'Usuário não existe'}), 404

    if user.senha == password:
        return jsonify({'message': 'Entrando'}), 200
    else:
        return jsonify({'message': 'Senha incorreta'}), 404

@user_controller.route("/registerUser", methods=["POST"])
def regist_user():
    request_data = request.get_json()

    # Verifique os campos obrigatórios
    if 'login' not in request_data or 'password' not in request_data or 'cpf' not in request_data or 'saldo' not in request_data:
        return jsonify({'message': 'Campos inválidos, verifique e tente novamente'}), 400

    login = request_data['login']
    password = request_data['password']
    saldo = request_data['saldo']
    cpf = request_data ['cpf']

    user_service.create_user(login,password,saldo,cpf)
    return jsonify({'message': 'Cadastrado'}), 200

