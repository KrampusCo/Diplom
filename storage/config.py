import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:12345@localhost:3306/flaskfiles'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
