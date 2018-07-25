from app.controllers.ControleAcidentesCSV import getBairrosMaisAcidentes


def getQtdTotalAcidente():
    return sum(getBairrosMaisAcidentes())


def getPercentualAcidenteBairro():
    listaBairros = ["AFOGADOS", "BAIRRO DO RECIFE", "BOA VIAGEM", "BOA VISTA", "CASA AMARELA", "CASA FORTE", "CORDEIRO",
                    "DERBY", "DOIS UNIDOS", "ENCRUZILHADA",
                    "ESPINHEIRO", "GRAÇAS", "ILHA DO LEITE", "ILHA DO RETIRO", "IPUTINGA", "MADALENA", "PARNAMIRIM",
                    "PINA", "SANTO AMARO", "SANTO ANTÔNIO",
                    "SÃO JOSÉ", "SOLEDADE", "TORRE"]
    x = getBairrosMaisAcidentes()
    y = getQtdTotalAcidente()
    listaFinal = []
    listagem = []
    for i in x:
        valor = (i * 100 / y)
        listagem.append(valor)
    for j in range(len(listaBairros)):
        maior = max(listagem)
        pos = listagem.index(maior)
        bairro = listaBairros[pos]
        listaFinal.append(str(bairro) + ": " + str(round(maior, 3)) + "%")
        listaBairros.remove(bairro)
        listagem.remove(maior)

    return listaFinal
