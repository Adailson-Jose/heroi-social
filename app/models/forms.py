from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, InputRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    mail = EmailField('email', [validators.DataRequired(), validators.Email()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")
