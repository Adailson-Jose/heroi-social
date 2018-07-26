from app import db
# Obs: nao sei que valores serao setados em: equipamento e fluxo_veiculo
class equipamento_fiscalizacao(db.Model):
    __tablename__ = "equipamento_fiscalizacao"

    codequip = db.Column(db.Integer, primary_key=True, autoincrement=True)
    equipamento = db.Column(db.String(100))
    velocidade_regulamentada = db.Column(db.String(5))
    endereco_codlocal = db.Column(db.Integer, db.ForeignKey('endereco.codlocal'))

    def __init__(self, codequip, equipamento, velocidade_regulamentada, endereco_codlocal):
        self.codequip = codequip
        self.equipamento = equipamento
        self.velocidade_regulamentada = velocidade_regulamentada
        self.endereco_codlocal = endereco_codlocal
