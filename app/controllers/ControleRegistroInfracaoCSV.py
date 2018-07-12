from app.models.RegistroInfracaoObjeto import registro_infracao
from app.persistence.EnderecoDao import getEnderecoDao
from app.persistence.RegistroInfracaoDao import postRegistroInfracao


def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, 'r')
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista


def inserirRegistroInfracao(nomeDoTxt='registro de infraçoes 2017(1-3).txt'):
    lista = lerTxt(nomeDoTxt)
    cont = 0
    for i in lista:
        i = i.replace('\n', '')
        i = i.split(';')
        print(i)
        if i[0] != 'datainfracao' and len(i) == 8:
            data_infracao = i[0]
            hora_infracao = i[1]
            data_implantacao = i[2]
            agente_equipamento = i[3]
            infracao_codinfracao = i[4]
            descricaoinfracao = i[5]
            amparolegal = i[6]
            localcometimento = i[7]

            codEndereco = getEnderecoDao(localcometimento, '', '')
            if codEndereco != False:
                for i in codEndereco:
                    objRegistroInfracao = registro_infracao(None, data_infracao, hora_infracao, data_implantacao,
                                                            agente_equipamento,
                                                            infracao_codinfracao, descricaoinfracao, amparolegal,
                                                            i.codlocal)
                    postRegistroInfracao(objRegistroInfracao)
                    cont += 1
        print(cont)
    return ("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont)))


print(inserirRegistroInfracao())