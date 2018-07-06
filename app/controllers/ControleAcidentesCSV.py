import csv
from app.models.AcidenteObjeto import acidente
from app.persistence.EnderecoDao import getEnderecoDao
from app.persistence.AcidenteDao import postAcidente


def lerCsv(nome_ficheiro):
    ficheiro = open(nome_ficheiro, 'r')
    reader = csv.reader(ficheiro)
    # ficheiro.close()
    return reader


'''
csv = lerCsv('tabela acidente com e s vítimas.csv')
for i in csv:
    i = i[0]
    i = i.split(';')

    if i[0] !='data_infracao' and len(i) == 8:
        data_abertura = i[0]
        hora_abertura = i[1]
        bairro = i[2]
        endereco = i[3]
        complemento = i[4]
        tipo_ocorrencia = i[5]
        quantidade_vitimas =i[6]
        descricao = i[7]
        tipo = i[8]
        latitude = i[9]
        longitude = i[10]
        print(endereco)

        codEndereco = getEnderecoDao(endereco)
        print(codEndereco)
        if codEndereco != False and codEndereco != None :
            objEquipamento = acidente(None, data_abertura, hora_abertura, tipo_ocorrencia,
                 quantidade_vitimas, descricao, codEndereco.codlocal, tipo)
            print(postAcidente(objEquipamento))
'''
