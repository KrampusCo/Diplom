from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

storageapp = Flask(__name__)
storageapp.config.from_object(Config)
db = SQLAlchemy(storageapp)
migrate = Migrate(storageapp, db)

from storageapp import routes
