from app import db
# Obs: nao sei que valores serao setados em: equipamento e fluxo_veiculo
class equipamento_fiscalizacao(db.Model):
    __tablename__ = "equipamento_fiscalizacao"

    cod_equipamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    localizacao = db.Column(db.String(100))
    tipo = db.Column(db.String(100))
    latitude = db.Column(db.String(12))
    longitude = db.Column(db.String(12))
    velocidade_regulamentada = db.Column(db.String(5))


    def __init__(self, cod_equipamento, localizacao, tipo, latitude, longitude, velocidade_regulamentada):
        self.cod_equipamento = cod_equipamento
        self.localizacao = localizacao
        self.tipo = tipo
        self.latitude = latitude
        self.longitude = longitude
        self.velocidade_regulamentada = velocidade_regulamentada
