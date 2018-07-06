from app import db
from app.models.EnderecoObjeto import endereco


def getEnderecoDao(stringEndereco):
    objEndereco = endereco.query.filter_by(local1=stringEndereco).first()

    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco


def postEndereco(objEndereco):
    db.session.add(objEndereco)
    if db.session.commit() == None:
        return True  # endereco foi inserido no banco
    return False
