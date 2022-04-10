from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField)
from wtforms.validators import InputRequired, Length


class NewShareForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), length(max=180)])
    language = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
