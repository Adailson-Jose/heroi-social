from app import db

class assinatura(db.Model):
    __tablename__ = "assinatura"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_entidade = db.Column(db.Integer)
    id_pacote_informacao = db.Column(db.Integer)
    data_compra = db.Column(db.String(10))
    validade = db.Column(db.String(10))
    preco_compra = db.Column(db.Float)

    def __init__(self, id_entidade, id, id_pacote_informacao, data_compra, validade, preco_compra):
        self.id = id
        self.id_entidade = id_entidade
        self.id_pacote_informacao = id_pacote_informacao
        self.data_compra = data_compra
        self.validade = validade
        self.preco_compra = preco_compra
