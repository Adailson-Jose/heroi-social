from app import db

class registro_infracao(db.Model):
    __tablename__ = "registro_infracao"

    codregistro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_infracao = db.Column(db.String(45))
    hora_infracao = db.Column(db.String(10))
    data_implantacao = db.Column(db.String(45))
    agente_equipamento = db.Column(db.String(45))
    infracao_codinfracao = db.Column(db.Integer)
    descricaoinfracao = db.Column(db.String(300))
    amparolegal = db.Column(db.String(45))
    endereco_codlocal = db.Column(db.Integer, db.ForeignKey('endereco.codlocal'))
    bairro = db.Column(db.String(45))


    def __init__(self, codregistro, data_infracao, hora_infracao, data_implantacao, agente_equipamento,
                 infracao_codinfracao, descricaoinfracao, amparolegal, endereco_codlocal, bairro):
        self.codregistro = codregistro
        self.data_infracao = data_infracao
        self.hora_infracao = hora_infracao
        self.data_implantacao = data_implantacao
        self.agente_equipamento = agente_equipamento
        self.infracao_codinfracao = infracao_codinfracao
        self.descricaoinfracao = descricaoinfracao
        self.amparolegal = amparolegal
        self.endereco_codlocal = endereco_codlocal
        self.bairro = bairro
