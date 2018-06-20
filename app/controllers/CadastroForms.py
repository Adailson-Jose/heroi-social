from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.fields.html5 import TelField


class CadastroForm(FlaskForm):
    mail = EmailField('email', [validators.DataRequired(), validators.Email(), validators.length(min=10, max=40)])
    password = PasswordField("password", validators=[DataRequired(), validators.length(min=8, max=25)])
    cnpj = StringField("cnpj", validators=[DataRequired(), validators.length(min=14, max=14)])
    telefone = TelField("telefone", validators=[DataRequired(), validators.length(min=8, max=12)])
    tipo_entidade = IntegerField("tipo_entidade", validators=[DataRequired(), validators.InputRequired()])
    razao_social = StringField("razao_social", validators=[DataRequired(), validators.length(min=0, max=50),
                                                           validators.input_required()])
