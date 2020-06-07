from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import user_repository
import User

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)



@app.route('/auth', methods=['POST'])
def auth():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)        
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    user = user_repository.find_user(email)
    if (user is None):
        return jsonify({"msg": "Login failed. Check your name and password"}), 401
        
    if (str(password) == str(user.password)):
        access_token = create_access_token(identity=user.id)
        return jsonify(user=user.name, token=access_token), 200 
    return jsonify({"msg": "Check your credentials and try again"}), 401

@app.route('/user', methods=['POST'])
def create_user():
    name = request.json.get('name', None)
    email = request.json.get('name', None)
    password = request.json.get('password', None)
    if not name:
        return jsonify({"msg": "Missing name parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    user_repository.users.insert_one({'name': name, 'email': email, 'password': password})


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
