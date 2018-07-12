from app.models.EquipamentoFiscalizacaoObjeto import equipamento_fiscalizacao
from app.persistence.EnderecoDao import getEnderecoDao
from app.persistence.EquipamentoDao import postEquipamento


def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, encoding="utf8")
    # ficheiro = open(nome_ficheiro,  "r")
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista


def inserirEquipamentos(nomeDoTxt='equipamentos-de-monitoramento-e-ficalizacao.txt'):
    reader = lerTxt(nomeDoTxt)
    cont = 0
    for i in reader:
        i = i.replace('\n', '')
        i = i.split(';')
        if i[0] != 'localizacao' and len(i) == 8:
            endereco = i[0]
            tipoEquipamento = i[1]
            latitude = i[2]
            longitude = i[3]
            velocidade = i[4]
            contrato = i[5]
            nome = i[6]
            fluxo_veiculo = i[7]

            codEndereco = getEnderecoDao(endereco, latitude, longitude)
            if codEndereco:
                for i in codEndereco:
                    objEquipamento = equipamento_fiscalizacao(None, tipoEquipamento, velocidade,
                                                              contrato, nome, fluxo_veiculo, i.codlocal)
                    postEquipamento(objEquipamento)
                    cont += 1
    return ("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont)))

# print(inserirEquipamentos())
