from app import db

class teste(db.Model):
    __tablename__= "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userNome = db.Column(db.String(16))
    password = db.Column(db.String(16))

    def __init__(self, userNome, password):
        self.nome = userNome
        self.password = password

    def __repr__(self):
        return '<User %r>'% self.userNome


class usuario(db.Model):
    __tablename__= "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userNome = db.Column(db.String(16))
    password = db.Column(db.String(16))

    def __init__(self, userNome, password):
        self.nome = userNome
        self.password = password

    def __repr__(self):
        return '<User %r>'% self.userNome
