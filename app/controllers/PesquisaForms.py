from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import validators

class pesquisaForm(FlaskForm):
    buscaBairro = StringField("buscaBairro", validators=[DataRequired(), validators.input_required()])