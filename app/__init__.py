from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db) #Cuida das migrações (CRUD)

manager = Manager(app) # Cuida dos comando que inicia a aplicação
manager.add_command('db', MigrateCommand)

from app.controllers import default
from app.models import tabelas


