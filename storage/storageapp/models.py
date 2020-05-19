from storageapp import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.LargeBinary)
