from app import db
from app.models.EnderecoObjeto import endereco


def getEnderecoDao(stringEndereco1, latitude, longitude):
    objEndereco = endereco.query.filter((endereco.local1 == stringEndereco1),
                                        (endereco.latitude == latitude),
                                        (endereco.longitude == longitude))
    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco


def getEnderecoDao(stringEndereco1, latitude, longitude, stringEndereco2):
    objEndereco = endereco.query.filter((endereco.local1 == stringEndereco1),
                                        (endereco.latitude == latitude),
                                        (endereco.longitude == longitude),
                                        (endereco.local2 == stringEndereco2))
    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco

def postEndereco(objEndereco):
    db.session.add(objEndereco)
    if db.session.commit() == None:
        return True  # endereco foi inserido no banco
    return False

# teste de consulta
# x=getEnderecoDao('AV CAXANGA','-8.0529196','-34.9164605')
# if x:
#    print(x)
# print(x)
