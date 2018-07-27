from app import db

class registro_infracao(db.Model):
    __tablename__ = "registro_infracao"

    codregistro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_infracao = db.Column(db.String(45))
    hora_infracao = db.Column(db.String(10))
    agente_equipamento = db.Column(db.String(45))
    infracao_codinfracao = db.Column(db.Integer)
    descricaoinfracao = db.Column(db.String(300))
    endereco_codlocal = db.Column(db.Integer, db.ForeignKey('endereco.codlocal'))

    def __init__(self, codregistro, data_infracao, hora_infracao, agente_equipamento,
                 infracao_codinfracao, descricaoinfracao, endereco_codlocal):
        self.codregistro = codregistro
        self.data_infracao = data_infracao
        self.hora_infracao = hora_infracao
        self.agente_equipamento = agente_equipamento
        self.infracao_codinfracao = infracao_codinfracao
        self.descricaoinfracao = descricaoinfracao
        self.endereco_codlocal = endereco_codlocal
