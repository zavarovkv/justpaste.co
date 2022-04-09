from app import app
from flask import render_template

from .texts import Texts


@app.route('/')
def index():
    return render_template('index.html',
                           title=Texts.TITLE,
                           description=Texts.DESCRIPTION
                           )
