from app.models.SemaforoObjeto import semaforo
from app.persistence.EnderecoDao import getEnderecoDao4
from app.persistence.SemafaroDao import postSemafaro
import time


def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, encoding="utf8")
    # ficheiro = open(nome_ficheiro,  "r")
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista


def inserirSemaforos(nomeDoTxt='semaforos.txt'):
    lista = lerTxt(nomeDoTxt)
    cont = 0
    for i in lista:
        i = i.replace('\n', '')
        i = i.split(';')
        if i[0] != 'semaforo' and len(i) == 9:
            codSemaforo = i[0]
            localizacao1 = i[1]
            localizacao2 = i[2]
            funcionamento = i[3]
            utilizacao = i[4]
            sinalsonoro = i[5]
            sinalizadorciclista = i[6]
            latitude = i[7]
            longitude = i[8]
            codEndereco = getEnderecoDao4(localizacao1, latitude, longitude, localizacao2)
            if codEndereco:
                for i in codEndereco:
                    print(i)
                    objSemaforo = semaforo(codSemaforo, funcionamento, sinalsonoro, sinalizadorciclista,
                                           utilizacao, i.codlocal)
                    postSemafaro(objSemaforo)
                    cont += 1
                    print(cont)
    print('*')
    print('**')
    print('***')
    print('****')
    time.sleep(9999)
    print(("Fim do time."))
    time.sleep(9999)
    return ("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont)))

#print(inserirSemaforos())
