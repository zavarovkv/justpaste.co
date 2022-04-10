from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length

from .config import Config


class NewShareForm(FlaskForm):
    title = StringField('Title', validators=[Length(max=255)])
    languageSelector = SelectField('Programming Language', coerce=str, choices=list(Config.PROGRAM_LANGUAGES.items()))
    # text = TextAreaField('Description', validators=[InputRequired(), Length(max=16000)])
