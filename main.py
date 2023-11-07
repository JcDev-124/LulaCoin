from flask import Flask
from controller.UserController import user_controller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/lulacoinsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.register_blueprint(user_controller)

if __name__ == "__main__":
    app.run(debug=True)
