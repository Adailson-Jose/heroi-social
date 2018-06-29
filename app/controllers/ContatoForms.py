from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired
from wtforms import validators, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.fields.html5 import TelField

class ContatoForm(FlaskForm):
    nome = StringField("Nome: *", validators=[DataRequired(), validators.length(min=3, max=35)])
    email = EmailField('email', [validators.DataRequired(), validators.Email(), validators.length(min=10, max=40)])
    entidade = StringField("Tipo de Entidade", validators=[DataRequired(), validators.InputRequired(), validators.length(min=0, max=1)])
    mensagem = TextAreaField("Mensagem",  validators=[DataRequired(), validators.length(min=0, max=250),
                                                           validators.input_required()])
