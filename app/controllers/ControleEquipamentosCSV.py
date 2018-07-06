import csv
from app.models.EquipamentoFiscalizacaoObjeto import equipamento_fiscalizacao
from app.persistence.EnderecoDao import getEnderecoDao
from app.persistence.EquipamentoDao import postEquipamento


def lerCsv(nome_ficheiro):
    ficheiro = open(nome_ficheiro, 'r')
    reader = csv.reader(ficheiro)
    # ficheiro.close()
    return reader


'''
csv = lerCsv('equipamentos-de-monitoramento-e-ficalizacao.csv')
for i in csv:
    i = i[0]
    i = i.split(';')
    if i[0] !='localizacao' and len(i) == 8:
        endereco = i[0]
        tipoEquipamento = i[1]
        latitude = i[2]
        longitude = i[3]
        velocidade = i[4]
        contrato = i[5]
        nome =i[6]
        fluxo_veiculo = i[7]

        codEndereco = getEnderecoDao(endereco).codlocal
        if codEndereco:
            objEquipamento = equipamento_fiscalizacao(None, tipoEquipamento, velocidade, contrato, nome, fluxo_veiculo, codEndereco)
            print(postEquipamento(objEquipamento))
'''
