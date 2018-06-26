from app import db

class entidade(db.Model):
    __tablename__ = "entidade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.Integer)
    estado = db.Column(db.Boolean)
    telefone = db.Column(db.Integer)
    tipo_entidade = db.Column(db.Integer)
    id_endereco = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    razao_social = db.Column(db.String(50))

    def __init__(self, id, cnpj, estado, telefone, tipo_entidade, id_endereco, id_usuario, razao_social):
        self.id = id
        self.cnpj = cnpj
        self.estado = estado
        self.telefone = telefone
        self.tipo_entidade = tipo_entidade
        self.id_endereco = id_endereco
        self.id_usuario = id_usuario
        self.razao_social = razao_social
