from app import db

class camera_transito(db.Model):
    __tablename__ = "camera_transito"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_endereco = db.Column(db.Integer)
    nome = db.Column(db.String(10))

    def __init__(self, cod, id_endereco, nome):
        self.cod = cod
        self.id_endereco = id_endereco
        self.nome = nome
