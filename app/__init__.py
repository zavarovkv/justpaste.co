from flask import Flask, request
from flask_babel import Babel
from hashids import Hashids
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
hashids = Hashids(salt=app.config['HASHIDS_SALT'])


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# hint with ears
from app import routes
