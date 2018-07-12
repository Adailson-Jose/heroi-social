from app import db
from app.models.EquipamentoFiscalizacaoObjeto import equipamento_fiscalizacao


def postEquipamento(equipamento):
    db.session.add(equipamento)
    if db.session.commit() == None:
        return True  # equipamento foi inserido no banco
    return False


def getEqupamentos():
    return equipamento_fiscalizacao.query.filter_by().all()
