from app import db
from app.models.RegistroInfracaoObjeto import registro_infracao


def postRegistroInfracao(registroInfracao):
    db.session.add(registroInfracao)
    if db.session.commit() == None:
        return True  # RegistroInfracao foi inserido no banco
    return False

def getRegistroInfracaoData(stringData):
    objRegistroInfracao = registro_infracao.query.filter((registro_infracao.data_infracao.like('%'+stringData+'%')))
    if objRegistroInfracao == None:
        return False  # não tem esse endereco no banco
    return objRegistroInfracao



def getRegistroInfracao():
    return registro_infracao.query.filter_by().all()
