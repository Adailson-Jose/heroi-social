from app import db

class endereco(db.Model):
    __tablename__ = "endereco"

    codlocal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    local1 = db.Column(db.String(100))
    local2 = db.Column(db.String(100))
    complemento = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    bairro = db.Column(db.String(20))
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))

    acidente = db.relationship('acidente', backref='endereco', lazy='dynamic')
    equipamento_fiscalizacao = db.relationship('equipamento_fiscalizacao', backref='endereco', lazy='dynamic')
    registro_infracao = db.relationship('registro_infracao', backref='endereco', lazy='dynamic')
    semaforo = db.relationship('semaforo', backref='endereco', lazy='dynamic')

    def __init__(self, codlocal, local1, local2, complemento, numero, bairro, latitude, longitude):
        self.codlocal = codlocal
        self.local1 = local1
        self.local2 = local2
        self.complemento = complemento
        self.numero = numero
        self.bairro = bairro
        self.latitude = latitude
        self.longitude = longitude
