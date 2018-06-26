from app import db

class sugestao(db.Model):
    __tablename__ = "sugestao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_entidade = db.Column(db.Integer)
    mensagem = db.Column(db.String(150))
    data = db.Column(db.String(10))

    def __init__(self, id, id_entidade, mensagem, data):
        self.id = id
        self.id_entidade = id_entidade
        self.mensagem = mensagem
        self.data = data
