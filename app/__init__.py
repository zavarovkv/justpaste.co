from flask import Flask, request
from flask_babel import Babel
from hashids import Hashids
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

babel = Babel(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
hashids = Hashids(salt=app.config['HASHIDS_KEY'])


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# hint with ears
from app import routes, models
