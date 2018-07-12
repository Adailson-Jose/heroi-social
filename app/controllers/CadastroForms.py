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
    rua = StringField("rua", validators=[DataRequired(), validators.input_required()])
    bairro = StringField("bairro", validators=[DataRequired(), validators.input_required()])
    cidade = StringField("cidade", validators=[DataRequired(), validators.input_required()])
    estado = StringField("estado", validators=[DataRequired(), validators.input_required()])
    numero = IntegerField("numero", validators=[DataRequired(), validators.input_required()])
    cep = TelField("cep", validators=[DataRequired(), validators.length(min=8, max=8)])
    # pesquisar como validar CEP (se ele é válido), e ver questão do tracinho
