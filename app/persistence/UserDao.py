from app.models.Tabelas import usuario
from app import db


def getUser(user):
    user = usuario.query.filter_by(email=user.email).first()
    if user == None:
        return False  # não tem esse user no banco
    return True


def postUser(user, entidade):
    db.session.add(user)
    db.session.add(entidade)
    if db.session.commit() == None:
        return True  # user foi inserido no banco
    return False
