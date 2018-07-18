from app import db
from app.models.AcidenteObjeto import acidente


def postAcidente(objAcidente):
    db.session.add(objAcidente)
    if db.session.commit() == None:
        return True  # objAcidente foi inserido no banco
    return False
def  getAcidentes():
    objAcidente = acidente.query.filter_by().all()
    if objAcidente == None:
        return None
    return objAcidente

def getAcidentesFiltro(stringData='', tipoDeDado=''):
    if stringData != '' and tipoDeDado !='':
        if tipoDeDado =='buscaData':
            objAcidente = acidente.query.filter((acidente.data_abertura.like('%'+stringData+'%')))
            if objAcidente == None:
                return None
            return objAcidente
        elif tipoDeDado =='buscaHora':
            objAcidente = acidente.query.filter((acidente.hora_abertura.like('%'+stringData+'%')))
            if objAcidente == None:
                return None
            return objAcidente
        elif tipoDeDado =='buscaTipoDeOcorrencia':
            objAcidente = acidente.query.filter((acidente.tipo_ocorrencia.like('%'+stringData+'%')))
            if objAcidente == None:
                return None
            return objAcidente
        elif tipoDeDado =='buscaTipo':
            objAcidente = acidente.query.filter((acidente.tipo.like('%'+stringData+'%')))
            if objAcidente == None:
                return None
            return objAcidente

    return None
