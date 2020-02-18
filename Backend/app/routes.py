from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from app.models import User
from flask_cors import CORS
from app import db


CORS(app)

app.config['JWT_SECRET_KEY'] = 'something-super-secret'  # Change this!
jwt = JWTManager(app)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/api/register', methods=["POST"])
def register():
    data = request.form
    username = data.get("username")
    password = data.get("password")
    password_salt_hash = generate_password_hash(password)
    try:
        new_user = User(username=username,
                        password_salt_hash=password_salt_hash)
        db.session.add(new_user)
        db.session.commit()
    except NameError:
        return jsonify({
            "status": "error",
            "message": "Could not add user: user exists"
        })

    return jsonify({
        "status": "success",
        "message": "User added successfully"
    }), 201


@app.route('/api/login', methods=["POST"])
def login():
    data = request.form
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_salt_hash, password):
        return jsonify({
            "status": "failed",
            "message": "Failed getting user"
        }), 401
    # Generate a token
    access_token = create_access_token(identity=username)
    return jsonify({
        "status": "success",
        "message": "login successful",
        "data": {
            "id": user.id,
            "token": access_token,
            "username": user.username
        }
    }), 200
