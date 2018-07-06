from app import db


class enderecoEntidade(db.Model):
    __tablename__ = "enderecoEntidade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rua = db.Column(db.String(35))
    bairro = db.Column(db.String(30))
    cidade = db.Column(db.String(30))
    estado = db.Column(db.String(35))
    numero = db.Column(db.Integer)
    cep = db.Column(db.Integer)

    def __init__(self, id, rua, bairro, cidade, estado, numero, cep):
        self.id = id
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.cep = cep
