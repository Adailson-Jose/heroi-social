from app import db
from app.models.AcidenteObjeto import acidente
from app.persistence.EnderecoDao import getEnderecoDao

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

        elif tipoDeDado == 'buscaQtd':
            objAcidente = acidente.query.filter((acidente.quantidade_vitimas.like('%' + stringData + '%')))
            if objAcidente == None:
                return None
            return objAcidente
        elif tipoDeDado == 'buscaLocal':

            objAcidente = acidente.query.filter("SELECT latitude, longitude, local1, codlocal FROM acidente, endereco where endereco_codlocal in(SELECT codlocal FROM endereco where local1 LIKE '%Boa viagem%') and codlocal = endereco_codlocal").all()

            if objAcidente == None:
                return None
            return objAcidente

    return None

def getAcidentesFiltro2(comp_select_ano, comp_select_mes, comp_select_bairro, comp_select_qtd_vitimas):

    if comp_select_ano != '' and comp_select_mes !='' and comp_select_bairro !=''and comp_select_qtd_vitimas !='':
        objAcidente = acidente.query.filter((acidente.quantidade_vitimas == comp_select_qtd_vitimas)).all()
        if objAcidente == None:
            return None
        return objAcidente

    return None


def getAcidentesFiltro3():
    pass
