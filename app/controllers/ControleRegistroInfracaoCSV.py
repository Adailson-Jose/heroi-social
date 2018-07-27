from app.models.RegistroInfracaoObjeto import registro_infracao
from app.persistence.EnderecoDao import getEnderecoDao
from app.persistence.RegistroInfracaoDao import getRegistroInfracaoData, postRegistroInfracao
import time

def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, encoding="utf8")
    # ficheiro = open(nome_ficheiro,  "r")
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista

def getTodosRegistrosDeInfracoes(data):
    datas = []
    listaInfracoes = getRegistroInfracaoData(data)

    for i in listaInfracoes:
        datas.append(i.infracao_codinfracao)

    return datas

def inserirRegistroInfracao(nomeDoTxt='registro de infraçoes 2017(1-3).txt'):
    lista = lerTxt(nomeDoTxt)
    cont = 0
    cont2 = 0
    for i in lista:
        i = i.replace('\n', '')
        i = i.split(';')
        if i[0] != 'DATAINFRACAO' and len(i) == 7:
            data_infracao = i[0]
            hora_infracao = i[1]
            agente_equipamento = i[2]
            infracao_codinfracao = i[3]
            descricaoinfracao = i[4]
            localcometimento = i[5][:-1]
            bairro = i[6]
            codEndereco = getEnderecoDao(localcometimento)
            if codEndereco != False:
                cont2 += 1
                print('contador interno: ', cont2)
                objRegistroInfracao = registro_infracao(None, data_infracao, hora_infracao,
                                                        agente_equipamento,
                                                        infracao_codinfracao, descricaoinfracao,
                                                        codEndereco.codlocal)
                postRegistroInfracao(objRegistroInfracao)
            cont += 1
        print('contador externo: ', cont)

    print(("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont2))))
    print('*')
    print('**')
    print('***')
    print('****')
    time.sleep(200000)
    print(("Fim do time."))
    time.sleep(200000)

    return ("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont2)))
# print(inserirRegistroInfracao())
