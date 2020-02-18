from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db
import random
import string

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_salt_hash = db.Column(db.String(300))

    def __repr__(self):
        return '<User {}>'.format(self.username)

