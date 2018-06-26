from app import db

class semaforo(db.Model):
    __tablename__ = "semaforo"

    cod_semaforo = db.Column(db.Integer, primary_key=True)
    id_endereco = db.Column(db.Integer)
    funcionamento = db.Column(db.String(10))
    utilizacao = db.Column(db.String(20))
    sinalsonoro = db.Column(db.String(1))
    sinalizadorciclista = db.Column(db.String(1))

    def __init__(self, cod_semaforo, id_endereco, funcionamento, utilizacao, sinalsonoro, sinalizadorciclista):
        self.cod_semaforo = cod_semaforo
        self.id_endereco = id_endereco
        self.funcionamento = funcionamento
        self.utilizacao = utilizacao
        self.sinalsonoro = sinalsonoro
        self.sinalizadorciclista = sinalizadorciclista
