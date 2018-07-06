from app import db

class acidente(db.Model):
    __tablename__ = "acidente"

    codacidente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_abertura = db.Column(db.String(45))
    hora_abertura = db.Column(db.String(45))
    tipo_ocorrencia = db.Column(db.String(45))
    quantidade_vitimas = db.Column(db.String(45))
    descricao = db.Column(db.String(45))
    endereco_codlocal = db.Column(db.Integer, db.ForeignKey('endereco.codlocal'))
    tipo = db.Column(db.String(45))

    def __init__(self, codacidente, data_abertura, hora_abertura, tipo_ocorrencia,
                 quantidade_vitimas, descricao, endereco_codlocal, tipo):
        self.codacidente = codacidente
        self.data_abertura = data_abertura
        self.hora_abertura = hora_abertura
        self.tipo_ocorrencia = tipo_ocorrencia
        self.quantidade_vitimas = quantidade_vitimas
        self.descricao = descricao
        self.endereco_codlocal = endereco_codlocal
        self.tipo = tipo
