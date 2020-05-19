from flask_restful import Resource, Api
from flask import request
from storageapp.models import File
from storageapp import db, storageapp
import requests

api = Api(storageapp)


class CreateFile(Resource):
    def post(self):

        try:
            new_file = File(file=1)
            db.session.add(new_file)
            db.session.commit()
        except:
            return{
                "Status": "gg",
                "success": "Error",
                
            }
        return{
            "Status": "Success",
            "success": "0",
            "file_id": new_file.id
        }


class UploadFile(Resource):
    def post(self):
        usertoken = request.headers["Authorization"]
        file_id = request.form["file_id"]
        server_id = 1
        byte = request.form["byte"]
        req = requests.request(
            method='POST',
            url='http://127.0.0.1:5000/check',
            headers={"Authorization": usertoken},
            data={'file_id': file_id,
                  'server_id': server_id},

        )
        if req.status_code == requests.codes.ok:
            if (req.json()["status"] == "Ok"):
                file = File.query.get(file_id)
                print(file.file)
                file.file = file.file + bytes(byte, 'utf-8')
                print(file.file) 
                db.session.commit()
                return{"status": "ok"}
            else:
                return{"status": "error file exists"}



api.add_resource(CreateFile, '/CreateFile')
api.add_resource(UploadFile, '/UploadFile')
