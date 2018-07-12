from app.persistence.EnderecoEntidadeDao import getIdMaxDao, postEnderecoEntidadeDao, getEnderecoEntidadeDao


def inserirEnderecoEntidade(objEnderecoEntidade):
    if postEnderecoEntidadeDao(objEnderecoEntidade):
        return True  # cadastro ok
    return False  # cadastro não ok


def getEnderecoEntidade(objEnderecoEntidade):
    objEnderecoEntidade = getEnderecoEntidadeDao(objEnderecoEntidade)
    if objEnderecoEntidade == False:
        return False  # erro
    return objEnderecoEntidade  # endereco já cadastrado


def getIdMax(objEnderecoEntidade):
    id = getIdMaxDao(objEnderecoEntidade)
    if id == False:
        return False  # erro
    return id  # endereco já cadastrado
