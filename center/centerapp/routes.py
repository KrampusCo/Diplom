from centerapp import db, centerapp
from centerapp.models import User, File, StorageServer
from flask import request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, jwt_refresh_token_required, get_raw_jwt,
)
from werkzeug.security import generate_password_hash, check_password_hash
import time
import datetime
import requests

centerapp.config['JWT_SECRET_KEY'] = 'something-super-secret'  # Change this!
centerapp.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(seconds=3006000)
jwt = JWTManager(centerapp)
api = Api(centerapp)


class UserRegistration(Resource):
    def post(self):
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        try:
            new_user = User(username=username,
                            password=password)

            db.session.add(new_user)
            db.session.commit()
        except NameError:
            return {
                "status": "error",
                "message": "Could not add user: user exists"
            }
        return {
            "operations": "User Registration",
            "status": "Success",
            "login": username
        }


class UserLogin(Resource):
    def post(self):
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return {
                "status": "failed",
                "message": "Failed getting user"
            }, 400
        access_token = create_access_token(identity=username)
        return {
            "operations": "User Login",
            "status": "success",
            "message": "login successful",
            "data": {
                "id": user.id,
                "token": access_token,
                "username": user.username
            }
        }


# class UserLogoutAccess(Resource):
#     @jwt_required
#     def post(self):
#         jti = get_raw_jwt()['jti']
#         try:
#             revoked_token = RevokedTokenModel(jti=jti)
#             revoked_token.add()
#             return {'message': 'Access token has been revoked'}
#         except:
#             return {'message': 'Something went wrong'}, 500


# class UserLogoutRefresh(Resource):
#     @jwt_refresh_token_required
#     def post(self):
#         jti = get_raw_jwt()['jti']
#         try:
#             revoked_token = RevokedTokenModel(jti=jti)
#             revoked_token.add()
#             return {'message': 'Refresh token has been revoked'}
#         except:
#             return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class AllUsers(Resource):
    def get(self):
        return User.return_all()

    def delete(self):
        return User.delete_all()


class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }


class AddFile(Resource):
    @jwt_required
    def post(self):
        user = User.query.filter_by(username=get_jwt_identity()).first()
        server = StorageServer.query.filter_by(id=1).first()
        name = request.form["name"]
        size = request.form["size"]
        key = request.form["key"]

        req = requests.request(
            method='POST',
            url='http://127.0.0.1:5001/CreateFile',
        )

        if req.status_code == requests.codes.ok:
            file_id = req.json()["file_id"]
        try:
            new_file = File(username_id=user.id,
                            server_id=server.id,
                            name=name,
                            size=size,
                            date=time.strftime('%Y-%m-%d %H:%M:%S'),
                            key=key,
                            file_id=file_id
                            )
            db.session.add(new_file)
            db.session.commit()
        except NameError:
            return {
                "status": "error",
                "message": "Could not add user: user exists"
            }
        return {
            "operations": "User Registration",
            "status": "Success",
            "server_ip": server.ip
        }


class ChekFileUser(Resource):
    @jwt_required
    def post(self):
        user = User.query.filter_by(username=get_jwt_identity()).first()
        file_id = request.form["file_id"]
        server_id = request.form["server_id"]
        file_exist = File.query.filter_by(username_id=user.id,
                                          file_id=file_id,
                                          server_id=server_id).first()
        print(user.id,"  ", file_id," ", server_id)
        if (file_exist):
            return {
                "operations": "Chek file user",
                "status": "Ok"
            }
        else:
            return {
                "operations": "Chek file user",
                "status": "Bad"
            }

class AllUserFile(Resource):
    @jwt_required
    def get(self):
        user = User.query.filter_by(username=get_jwt_identity()).first()
        return File.return_all(user.id)

api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
# api.add_resource(UserLogoutAccess, '/logout/access')
# api.add_resource(UserLogoutRefresh, '/logout/refresh')
api.add_resource(TokenRefresh, '/token/refresh')
api.add_resource(AllUsers, '/users')
api.add_resource(SecretResource, '/secret')
api.add_resource(AddFile, '/addfile')
api.add_resource(ChekFileUser, '/check')
api.add_resource(AllUserFile, '/AllUserFile')