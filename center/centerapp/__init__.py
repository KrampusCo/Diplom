from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


centerapp = Flask(__name__)
centerapp.config.from_object(Config)
db = SQLAlchemy(centerapp)
migrate = Migrate(centerapp, db)

from centerapp import routes
