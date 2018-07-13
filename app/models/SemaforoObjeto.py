from app import db

class semaforo(db.Model):
    __tablename__ = "semaforo"

    codsemaforo = db.Column(db.Integer, primary_key=True)
    funcionamento = db.Column(db.String(45))
    sinalsonoro = db.Column(db.String(45))
    sinalizadorciclista = db.Column(db.String(145))
    utilizacao = db.Column(db.String(45))
    endereco_codlocal = db.Column(db.Integer, db.ForeignKey('endereco.codlocal'))

    def __init__(self, codsemaforo, funcionamento,
                 sinalsonoro, sinalizadorciclista, utilizacao, endereco_codlocal):
        self.codsemaforo = codsemaforo
        self.funcionamento = funcionamento
        self.sinalsonoro = sinalsonoro
        self.sinalizadorciclista = sinalizadorciclista
        self.utilizacao = utilizacao
        self.endereco_codlocal = endereco_codlocal
