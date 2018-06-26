from app import db

class pacote_informacao(db.Model):
    __tablename__ = "pacote_informacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_pacote = db.Column(db.String(30))
    tipo_entidade = db.Column(db.Integer)
    ano_pacote = db.Column(db.String(10))
    duracao = db.Column(db.String(10))
    descricao = db.Column(db.String(50))
    valor = db.Column(db.Float)

    def __init__(self, id, nome_pacote, tipo_entidade, ano_pacote, duracao, descricao, valor):
        self.id = id
        self.nome_pacote = nome_pacote
        self.tipo_entidade = tipo_entidade
        self.ano_pacote = ano_pacote
        self.duracao = duracao
        self.descricao = descricao
        self.valor = valor