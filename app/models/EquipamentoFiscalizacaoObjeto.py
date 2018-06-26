from app import db
# Obs: nao sei que valores serao setados em: equipamento e fluxo_veiculo
class equipamento_fiscalizacao(db.Model):
    __tablename__ = "equipamento_fiscalizacao"

    cod_equipamento = db.Column(db.Integer, primary_key=True)
    id_endereco = db.Column(db.Integer)
    velociade = db.Column(db.Integer)
    equipamento = ''
    fluxo_veiculo = ''

    def __init__(self, cod_equipamento, id_endereco, velociade, equipamento, fluxo_veiculo):
        self.cod_equipamento = cod_equipamento
        self.id_endereco = id_endereco
        self.velociade = velociade
        self.equipamento = equipamento
        self.fluxo_veiculo = fluxo_veiculo
