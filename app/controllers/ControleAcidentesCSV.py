from app.models.AcidenteObjeto import acidente
from app.models.EnderecoObjeto import endereco
from app.persistence.EnderecoDao import getEnderecoID, getEnderecoDao
from app.persistence.AcidenteDao import postAcidente, getAcidentes


def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, encoding="utf8")
    # ficheiro = open(nome_ficheiro, "r")
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista

def getTodosAcidentes():
    coordenadas = []
    ruas = []
    listaLatitude = []
    listaLongitude = []
    listaAcidente = getAcidentes()
    for i in listaAcidente:
        endereco  = getEnderecoID(i.endereco_codlocal)
        for endereco in endereco:
            if len((endereco.latitude).split('.')) == 2 and len((endereco.longitude).split('.')) == 2:
                latitude = float(endereco.latitude)
                longitude = float(endereco.longitude)
                listaLatitude.append(latitude)
                listaLongitude.append(longitude)
                ruas.append(i.data_abertura)
    coordenadas.append(listaLatitude)
    coordenadas.append(listaLongitude)
    coordenadas.append(ruas)
    return coordenadas

def inseriAcidentes(nomeDoTxt='tabela acidente com  vítimas(2014-2016).txt'):
    lista = lerTxt(nomeDoTxt)
    cont = 0
    for i in lista:
        i = i.replace('\n', '')
        i = i.split(';')
        if i[0] != 'data_abertura' and len(i) == 11:
            data_abertura = i[0]
            hora_abertura = i[1]
            bairro = i[2]
            endereco = i[3]
            complemento = i[4]
            tipo_ocorrencia = i[5]
            quantidade_vitimas = i[6]
            descricao = i[7]
            tipo = i[8]
            latitude = i[9]
            longitude = i[10]
            codEndereco = getEnderecoDao(endereco, latitude, longitude)
            if codEndereco:
                for i in codEndereco:
                    objAcidente = acidente(None, data_abertura, hora_abertura, tipo_ocorrencia,
                                           quantidade_vitimas, descricao, i.codlocal, tipo)
                    postAcidente(objAcidente)
                    cont += 1
        print(cont)
    return ("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont)))

#print(inseriAcidentes())
