from datetime import datetime
from centerapp import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(300))
    users = db.relationship('File', backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), User.query.all()))}


class StorageServer(db.Model):
    __tablename__ = 'storage_servers'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer)
    ip = db.Column(db.String(20), unique=True)
    storageservers = db.relationship('File', backref='storageServer')


class File(db.Model):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    username_id = db.Column(db.Integer,
                            db.ForeignKey('users.id'),
                            nullable=True)
    server_id = db.Column(db.Integer,
                          db.ForeignKey('storage_servers.id'),
                          nullable=True)
    file_id = db.Column(db.Integer)
    name = db.Column(db.String(200))
    size = db.Column(db.Integer)
    date = db.Column(db.DateTime, nullable=False)
    key = db.Column(db.String(200))

    @classmethod
    def return_all(cls, id):
        def to_json(x):
            return {
                'name': x.name,
                'size': x.size,
                'date': str(x.date),
            }
        return {'files': list(map(lambda x: to_json(x), File.query.filter_by(username_id=id).all()))}
