import csv
from app.models.EquipamentoFiscalizacaoObjeto import equipamento_fiscalizacao
from app import db

def lerCsv(nome_ficheiro):
    ficheiro = open(nome_ficheiro, 'r')
    reader = csv.reader(ficheiro)
    #ficheiro.close()
    return reader

def postEquipamento(equipamento):
    db.session.add(equipamento)
    if db.session.commit() == None:
        return True  # equipamento foi inserido no banco
    return False

'''csv = lerCsv('monitoramentoficalizacao.csv')
for i in csv:
    i = i[0]
    i = i.split(';')
    if i[0] !='localizacao' and len(i) ==5:
        print(i)
        end = i[0]
        tipo = i[1]
        latitude = i[2]
        longitude =i[3]
        velocidade = i[4]
        
        obj = equipamento_fiscalizacao(None,end,tipo, latitude, longitude, velocidade)
        print(postEquipamento(obj))
'''
'''def getEqupamentos():
    return equipamento_fiscalizacao.query.filter_by().all()'''
