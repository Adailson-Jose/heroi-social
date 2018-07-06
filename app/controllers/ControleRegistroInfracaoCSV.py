import csv
from app.models.RegistroInfracaoObjeto import registro_infracao
from app.persistence.EnderecoDao import getEnderecoDao
from app.persistence.RegistroInfracaoDao import postRegistroInfracao


def lerCsv(nome_ficheiro):
    ficheiro = open(nome_ficheiro, 'r')
    reader = csv.reader(ficheiro)
    # ficheiro.close()
    return reader


'''
csv = lerCsv('registro de infraçoes 2016.csv')
for i in csv:
    i = i[0]
    i = i.split(';')

    if i[0] !='data_infracao' and len(i) == 8:
        data_infracao = i[0]
        hora_infracao = i[1]
        data_implantacao = i[2]
        agente_equipamento = i[3]
        infracao_codinfracao = i[4]
        descricaoinfracao = i[5]
        amparolegal =i[6]
        localcometimento = i[7]
        print(localcometimento)

        codEndereco = getEnderecoDao(localcometimento)
        print(codEndereco)
        if codEndereco != False and codEndereco != None :
            objEquipamento = registro_infracao(None, data_infracao, hora_infracao, data_implantacao, agente_equipamento,
                 infracao_codinfracao, descricaoinfracao, amparolegal, codEndereco.codlocal)
            print(postRegistroInfracao(objEquipamento))
'''
