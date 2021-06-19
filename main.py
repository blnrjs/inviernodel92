# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from models.users import Users

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to Invierno del 92 "


@app.route('/inviernodel92/users.browser/<int:id_user>', methods=['GET'])
def loggin_user(id_user):
    user = Users(request.json)
    user_id = user.browse_user(id_user)
    return jsonify({'user_id': user_id}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
