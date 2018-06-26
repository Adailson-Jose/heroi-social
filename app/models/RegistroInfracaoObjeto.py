from app import db

class registro_infracao(db.Model):
    __tablename__ = "registro_infracao"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_endereco = db.Column(db.Integer)
    cod_infracao = db.Column(db.Integer)
    agente_equipamento = db.Column(db.String(50))
    hora_infracao = db.Column(db.String(10))
    data_infracao = db.Column(db.String(10))
    data_implantacao = db.Column(db.String(10))

    def __init__(self, cod, id_endereco, cod_infracao, agente_equipamento, hora_infracao, data_infracao,
                 data_implantacao):
        self.cod = cod
        self.id_endereco = id_endereco
        self.cod_infracao = cod_infracao
        self.agente_equipamento = agente_equipamento
        self.hora_infracao = hora_infracao
        self.data_infracao = data_infracao
        self.data_implantacao = data_implantacao

