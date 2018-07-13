from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField


class PagamentoForm(FlaskForm):
    mail = EmailField('email', [validators.DataRequired(), validators.Email(), validators.length(min=10, max=40)])
    password = PasswordField("password", validators=[DataRequired(), validators.length(min=8, max=25)])
