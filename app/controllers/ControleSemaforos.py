from app.models.SemaforoObjeto import semaforo
from app.models.EnderecoObjeto import endereco
from app.persistence.SemafaroDao import postSemafaro, getSemafaros
from app.persistence.EnderecoDao import getEnderecoID, getEnderecoDao2

def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, encoding="utf8")
    # ficheiro = open(nome_ficheiro, "r")
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista

def getTodosSemaforos():
    coordenadas = []
    ruas = []
    listaLatitude = []
    listaLongitude = []
    listaSemaforo = getSemafaros()
    for i in listaSemaforo:
        endereco  = getEnderecoID(i.endereco_codlocal)
        for endereco in endereco:
            if len((endereco.latitude).split('.')) == 2 and len((endereco.longitude).split('.')) == 2:
                latitude = float(endereco.latitude)
                longitude = float(endereco.longitude)
                listaLatitude.append(latitude)
                listaLongitude.append(longitude)
                ruas.append(endereco.local1 +' (...'+ i.utilizacao+'...)')
    coordenadas.append(listaLatitude)
    coordenadas.append(listaLongitude)
    coordenadas.append(ruas)
    return coordenadas

def inseriSemaforos(nomeDoTxt='semaforos.txt'):
    lista = lerTxt(nomeDoTxt)
    cont = 0
    for i in lista:
        i = i.replace('\n', '')
        i = i.split(';')
        if i[0] != 'semaforo' and len(i) == 9:
            codsemaforo = i[0]
            localizacao1 = i[1]
            localizacao2 = i[2]
            funcionamento = i[3]
            utilizacao = i[4]
            sinalsonoro = i[5]
            sinalizadorciclista = i[6]
            Latitude = i[7]
            Longitude = i[8]

            codEndereco = getEnderecoDao2(localizacao1,Latitude, Longitude,localizacao2)
            if codEndereco:
                for i in codEndereco:
                    objSemaforo = semaforo(codsemaforo, funcionamento, sinalsonoro, sinalizadorciclista, utilizacao, i.codlocal)
                    postSemafaro(objSemaforo)
                    cont += 1
        print(cont)
    return ("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont)))

#print(inseriSemaforos())
