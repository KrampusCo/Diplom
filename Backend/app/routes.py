from app import app
from flask import Flask, jsonify, request
from flask_login import current_user, login_user
from app.models import User
from flask_cors import CORS

CORS(app)


@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = request.form
    if current_user.is_authenticated:
        return request.data
    user = User.query.filter_by(username=form['username']).first()
    if user is None or not user.check_password(form['password']):
        return jsonify("bb")
    return jsonify("yes")
