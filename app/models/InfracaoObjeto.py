from app import db

class infracao(db.Model):
    __tablename__ = "infracao"

    cod_infracao = db.Column(db.Integer, primary_key=True)
    amaparo_legal = db.Column(db.String(50))
    descricao_infracao = db.Column(db.String(300))

    def __init__(self, cod_infracao, amaparo_legal, descricao_infracao):
        self.cod_infracao = cod_infracao
        self.amaparo_legal = amaparo_legal
        self.descricao_infracao = descricao_infracao
