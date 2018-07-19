from app.models.AcidenteObjeto import acidente
from app.persistence.EnderecoDao import getEnderecoID, getEnderecoDao
from app.persistence.AcidenteDao import postAcidente, getAcidentesFiltro, getAcidentes


def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, encoding="utf8")
    # ficheiro = open(nome_ficheiro, "r")
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista

def getTodosAcidentesFiltro(dados='', tipoDeDado=''):
    coordenadas = []
    ruas = []
    listaLatitude = []
    listaLongitude = []
    listaAcidente = getAcidentesFiltro(dados, tipoDeDado)
    if listaAcidente != None:
        for i in listaAcidente:
            endereco = getEnderecoID(i.endereco_codlocal)
            for endereco in endereco:
                if len((endereco.latitude).split('.')) == 2 and len((endereco.longitude).split('.')) == 2:
                    latitude = float(endereco.latitude)
                    longitude = float(endereco.longitude)
                    listaLatitude.append(latitude)
                    listaLongitude.append(longitude)
                    ruas.append(endereco.local1)
        coordenadas.append(listaLatitude)
        coordenadas.append(listaLongitude)
        coordenadas.append(ruas)
        return coordenadas
    return None

def getTodosAcidentes():
    coordenadas = []
    ruas = []
    listaLatitude = []
    listaLongitude = []
    listaAcidente = getAcidentes()
    if listaAcidente != None:
        for i in listaAcidente:
            endereco = getEnderecoID(i.endereco_codlocal)
            for endereco in endereco:
                if len((endereco.latitude).split('.')) == 2 and len((endereco.longitude).split('.')) == 2:
                    latitude = float(endereco.latitude)
                    longitude = float(endereco.longitude)
                    listaLatitude.append(latitude)
                    listaLongitude.append(longitude)
                    ruas.append(endereco.local1)
        coordenadas.append(listaLatitude)
        coordenadas.append(listaLongitude)
        coordenadas.append(ruas)
        return coordenadas
    return None

def getMesesAcidentes():
    listaAcidente = getAcidentes()

    dic_meses ={}
    if listaAcidente != None:
        for i in listaAcidente:
            data = (i.data_abertura).split("/")
            if len(data) != 1:
              mes = data[1]
              if mes in dic_meses:
                dic_meses[mes] += 1
              else:
                dic_meses[mes] = 1
    if len(dic_meses) != 0:
      return dic_meses.keys(), dic_meses.values()
    return None, None

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
