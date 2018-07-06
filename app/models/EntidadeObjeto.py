from app import db
from app.models.EnderecoObjetoEntidade import enderecoEntidade
from app.models.UsuarioObjeto import usuario

class entidade(db.Model):
    __tablename__ = "entidade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.String(14), unique=True)
    estado = db.Column(db.Boolean)
    telefone = db.Column(db.Integer)
    tipo_entidade = db.Column(db.Integer)
    razao_social = db.Column(db.String(50))

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    id_endereco = db.Column(db.Integer, db.ForeignKey('enderecoEntidade.id'))

    def __init__(self, id, cnpj, estado, telefone, tipo_entidade, id_endereco, id_usuario, razao_social):
        self.id = id
        self.cnpj = cnpj
        self.estado = estado
        self.telefone = telefone
        self.tipo_entidade = tipo_entidade
        self.id_endereco = id_endereco
        self.id_usuario = id_usuario
        self.razao_social = razao_social
