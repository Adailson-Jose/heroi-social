from app.models.EquipamentoFiscalizacaoObjeto import equipamento_fiscalizacao
from app.persistence.EnderecoDao import getEnderecoDao, getEnderecoID
from app.persistence.EquipamentoDao import postEquipamento, getEqupamentos


def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, encoding="utf8")
    # ficheiro = open(nome_ficheiro,  "r")
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista


def getTodosEquipamentos():
    coordenadas = []
    ruas = []
    listaLatitude = []
    listaLongitude = []
    listaEquipamentos = getEqupamentos()
    for i in listaEquipamentos:
        endereco  = getEnderecoID(i.endereco_codlocal)
        for endereco in endereco:
            if len((endereco.latitude).split('.')) == 2 and len((endereco.longitude).split('.')) == 2:
                latitude = float(endereco.latitude)
                longitude = float(endereco.longitude)
                listaLatitude.append(latitude)
                listaLongitude.append(longitude)
                ruas.append(endereco.local1 +' (...'+ i.equipamento+'...)')
    coordenadas.append(listaLatitude)
    coordenadas.append(listaLongitude)
    coordenadas.append(ruas)
    return coordenadas

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
