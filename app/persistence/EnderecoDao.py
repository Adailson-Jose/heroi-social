from app import db
from app.models.EnderecoObjeto import endereco


def getEnderecoDao3(stringEndereco1, latitude, longitude):
    objEndereco = endereco.query.filter((endereco.local1 == stringEndereco1),
                                        (endereco.latitude == latitude),
                                        (endereco.longitude == longitude))
    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco


def getEnderecoDao4(stringEndereco1, latitude, longitude, stringEndereco2):
    objEndereco = endereco.query.filter((endereco.local1 == stringEndereco1),
                                        (endereco.latitude == latitude),
                                        (endereco.longitude == longitude),
                                        (endereco.local2 == stringEndereco2))
    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco


def getEnderecoDao2(stringEndereco1, stringEndereco2):
    objEndereco = endereco.query.filter((endereco.local1 == stringEndereco1), (endereco.bairro == stringEndereco2)).first()
    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco

def getEnderecoDao(stringEndereco1):
    objEndereco = endereco.query.filter((endereco.local1.like('%' + stringEndereco1 + '%'))).first()
    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco


def getEnderecoID(stringid):
    objEndereco = endereco.query.filter(endereco.codlocal == stringid)
    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco


def postEndereco(objEndereco):
    db.session.add(objEndereco)
    if db.session.commit() == None:
        return True  # endereco foi inserido no banco
    return False


def getEnderecoLocal(bairro):
    objEndereco = endereco.query.filter(endereco.bairro == bairro)
    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco
