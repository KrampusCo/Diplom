import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3307/testFlask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
