from app import app
from flask import Flask, jsonify, request
from app.models import User
from flask_cors import CORS
from app import db

CORS(app)


@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    form = request.form
    user = User.query.filter_by(username=form['username']).first()
    if user is None or not user.check_password(form['password']):
        return jsonify("bb")
    return jsonify("yes")


@app.route('/api/logout')
def logout():
    return jsonify("logout")


@app.route('/api/register', methods=["POST"])
def register():
    data = request.form
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    try:
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
    except error:
        return jsonify({
            "status": "error",
            "message": "Could not add user"
        })

    return jsonify({
        "status": "success",
        "message": "User added successfully"
    }), 201
