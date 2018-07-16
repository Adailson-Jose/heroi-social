from app.models.UsuarioObjeto import usuario
from app import db

def getUserDao(user):
    user = usuario.query.filter_by(email=user.email).first()
    if user == None:
        return False  # não tem esse user no banco
    print(user)
    return user


def getIdMaxDao(user):
    user = usuario.query.count()
    if user == None:
        return False  # não tem esse user no banco
    return user


def postUser(user, entidade):
    db.session.add(user)
    db.session.commit()
    db.session.add(entidade)
    if db.session.commit() == None:
        return True  # user foi inserido no banco
    return False
