from app import db


class usuario(db.Model):
    __tablename__= "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(25))
    password = db.Column(db.String(16))

    def __init__(self, email, password):
        self.email = email
        self.password = password


class entidade(db.Model):
    __tablename__ = "entidade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.Integer)
    estado = db.Column(db.Boolean)
    telefone = db.Column(db.Integer)
    tipo_entidade = db.Column(db.Integer)
    id_endereco = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    razao_social = db.Column(db.String(25))

class endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rua = db.Column(db.String(25))
    bairro = db.Column(db.String(25))
    cidade = db.Column(db.String(25))
    estado = db.Column(db.String(25))
    numero = db.Column(db.Integer)
    cep = db.Column(db.Integer)


