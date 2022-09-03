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
            Length(max=Config.TITLE_MAX_LENGTH)
        ]
    )
    languageSelector = SelectField(
        'Programming Language',
        coerce=str,
        choices=list(Config.PROGRAM_LANGUAGES.items())
    )
    privacySelector = SelectField(
        'Privacy',
        coerce=str,
        choices=list(Config.PRIVACY_VARIANTS.items())
    )
    editor = TextAreaField(
        'Description',
        validators=[
            InputRequired(),
            Length(max=Config.EDITOR_MAX_LENGTH)
        ]
    )

    # Special field for detect bots (nh = noHuman)
    nh = StringField(
        'No Human',
        validators=[
            Length(max=Config.TITLE_MAX_LENGTH)
        ]
    )
