from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

app = Flask(__name__)
app.config.from_object(Config)
cache = Cache(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db,cache)

from app import routes
from app.model import product