from app import db

class infracao(db.Model):
    __tablename__ = "infracao"

    codinfracao = db.Column(db.Integer, primary_key=True)
    descricao_infracao = db.Column(db.String(100))

    def __init__(self, codinfracao, descricao_infracao):
        self.codinfracao = codinfracao
        self.descricao_infracao = descricao_infracao
