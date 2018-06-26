from app import db

class acidente(db.Model):
    __tablename__ = "acidente"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_endereco = db.Column(db.Integer)
    cod_envolvido = db.Column(db.Integer)
    # talvez precisemos ajustar a classe atual de endereco
    # adicionando os campos latitude e longitude
    tipo = db.Column(db.String(50))
    situacao = db.Column(db.String(50))
    data = db.Column(db.String(10))
    hora = db.Column(db.String(10))
    natureza = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    qtd_vitmas = db.Column(db.Integer)
    qtd_vitmas_fatais = db.Column(db.Integer)

    def __init__(self, cod, cod_envolvido, id_endereco, tipo, situacao, data, hora, natureza, descricao, qtd_vitmas,
                 qtd_vitmas_fatais):
        self.cod = cod
        self.cod_envolvido = cod_envolvido
        self.id_endereco = id_endereco
        self.tipo = tipo
        self.situacao = situacao
        self.data = data
        self.hora = hora
        self.natureza = natureza
        self.qtd_vitmas = qtd_vitmas
        self.qtd_vitmas_fatais = qtd_vitmas_fatais
