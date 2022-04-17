from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length

from .config import Config


class NewShareForm(FlaskForm):
    # Main fields
    title = StringField(
        'Title',
        validators=[
            InputRequired(),
            Length(max=Config.TITLE_MAX_LEN)
        ]
    )
    languageSelector = SelectField(
        'Programming Language',
        coerce=str,
        choices=list(Config.PROGRAM_LANGUAGES.items())
    )
    editor = TextAreaField(
        'Description',
        validators=[
            InputRequired(),
            Length(max=Config.EDITOR_MAX_LEN)
        ]
    )

    # Special field for detect bots (nh = noHuman)
    nh = StringField(
        'No Human',
        validators=[
            Length(max=Config.TITLE_MAX_LEN)
        ]
    )
