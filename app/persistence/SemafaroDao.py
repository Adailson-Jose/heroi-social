from app import db
from app.models.SemaforoObjeto import semaforo


def postSemafaro(objSemafaro):
    db.session.add(objSemafaro)
    if db.session.commit() == None:
        return True  # objSemafaro foi inserido no banco
    return False


def getSemafaros():
    return semaforo.query.filter_by().all()
