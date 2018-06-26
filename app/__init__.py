from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db) #Cuida das migrações (CRUD)

manager = Manager(app) # Cuida dos comando que inicia a aplicação
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)

from app.models import UsuarioObjeto, EnumTipoEntidade, EntidadeObjeto, AcidenteObjeto, AssinaturaObjeto, CameraTransitoObjeto, \
    CoordenadasObjeto, EnderecoObjeto, EnvolvidoObjeto, EquipamentoFiscalizacaoObjeto, InfracaoObjeto, PacoteInformacaObjeto, \
    SemaforoObjeto, SugestaoObjeto, RegistroInfracaoObjeto
from app.persistence import UserDao
from app.controllers import UserControllers, LoginForms, CadastroForms, ContatoForms
from app.api import Login, Cadastro, Sair, Principal, Sobre, Base, Contato, Index, LouderUser, GraficoBarras,\
    GraficoLinha, GraficoPizza, MapaAcidentes
