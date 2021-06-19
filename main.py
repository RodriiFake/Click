#--coding:utf-8 --
from flask import Flask, request, jsonify, abort
from models.users import Users
app = Flask(__name__)
@app.route('/')
def index():
    return "Bienvenido"

@app.route('/click/users.browse/<int:id_user>',methods=['GET'])
def loggin_user(id_user):
    user = Users({'id_user':id_user})
    user_id = user.browse_user(id_user)

    return jsonify({'user_id': user_id}), 200

def loggin_user():
    user = Users()
    columns_id = user.browse_columns()
    return jsonify({'Colums_id': columns_id}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)