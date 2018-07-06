from app import db
from app.models.AcidenteObjeto import acidente


def postAcidente(objAcidente):
    db.session.add(objAcidente)
    if db.session.commit() == None:
        return True  # objAcidente foi inserido no banco
    return False


def getAcidentes():
    return acidente.query.filter_by().all()
