from app import db

class envolvido(db.Model):
    __tablename__ = "envolvido"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qtd_auto = db.Column(db.Integer)
    qtd_moto = db.Column(db.Integer)
    qtd_ciclom = db.Column(db.Integer)
    qtd_ciclista = db.Column(db.Integer)
    qtd_pedestre = db.Column(db.Integer)
    qtd_onibus = db.Column(db.Integer)
    qtd_caminhao = db.Column(db.Integer)
    qtd_viatura = db.Column(db.Integer)
    qtd_outros = db.Column(db.Integer)

    def __init__(self, cod, qtd_auto, qtd_moto, qtd_ciclom, qtd_ciclista, qtd_pedestre, qtd_onibus, qtd_caminhao,
                 qtd_viatura, qtd_outros):
        self.cod = cod
        self.qtd_auto = qtd_auto
        self.qtd_moto = qtd_moto
        self.qtd_ciclom = qtd_ciclom
        self.qtd_ciclista = qtd_ciclista
        self.qtd_pedestre = qtd_pedestre
        self.qtd_onibus = qtd_onibus
        self.qtd_caminhao = qtd_caminhao
        self.qtd_viatura = qtd_viatura
        self.qtd_outros = qtd_outros
