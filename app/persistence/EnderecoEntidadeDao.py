from app import db
from app.models.EnderecoObjetoEntidade import enderecoEntidade


def getIdMaxDao(endereco):
    endereco = enderecoEntidade.query.count()
    if endereco == None:
        return False  # não tem esse endereco no banco
    return endereco


def getEnderecoEntidadeDao(objEnderecoEntidade):
    objEnderecoEntidade = enderecoEntidade.query.filter_by(rua=objEnderecoEntidade.rua,
                                                           bairro=objEnderecoEntidade.bairro,
                                                           cidade=objEnderecoEntidade.cidade,
                                                           estado=objEnderecoEntidade.estado,
                                                           numero=objEnderecoEntidade.numero,
                                                           cep=objEnderecoEntidade.cep).first()
    if objEnderecoEntidade == None:
        return False  # não tem esse endereco no banco
    return objEnderecoEntidade


def postEnderecoEntidadeDao(objEnderecoEntidade):
    db.session.add(objEnderecoEntidade)
    if db.session.commit() == None:
        return True  # endereco foi inserido no banco
    return False
