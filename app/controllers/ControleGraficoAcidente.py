from app.persistence.AcidenteDao import getAcidentesMes


def getTodosAcidenteAno(ano=''):
    sqlAno = getAcidentesMes(ano)
    JAN = 0
    FEB = 0
    MAR = 0
    APR = 0
    MAY = 0
    JUN = 0
    JUL = 0
    AUG = 0
    SEP = 0
    OCT = 0
    NOV = 0
    DEC = 0
    if sqlAno != None:
        for i in sqlAno:
            if '01' == i.data_abertura[3:-5] or '1' == i.data_abertura[3:-5]:
                JAN += 1
            elif '02' == i.data_abertura[3:-5] or '2' == i.data_abertura[3:-5]:
                FEB += 1
            elif '03' == i.data_abertura[3:-5] or '3' == i.data_abertura[3:-5]:
                MAR += 1
            elif '04' == i.data_abertura[3:-5] or '4' == i.data_abertura[3:-5]:
                APR += 1
            elif '05' == i.data_abertura[3:-5] or '5' == i.data_abertura[3:-5]:
                MAY += 1
            elif '06' == i.data_abertura[3:-5] or '6' == i.data_abertura[3:-5]:
                JUN += 1
            elif '07' == i.data_abertura[3:-5] or '7' == i.data_abertura[3:-5]:
                JUL += 1
            elif '08' == i.data_abertura[3:-5] or '8' == i.data_abertura[3:-5]:
                AUG += 1
            elif '09' == i.data_abertura[3:-5] or '9' == i.data_abertura[3:-5]:
                SEP += 1
            elif '10' == i.data_abertura[3:-5] or '10' == i.data_abertura[3:-5]:
                OCT += 1
            elif '11' == i.data_abertura[3:-5] or '11' == i.data_abertura[3:-5]:
                NOV += 1
            else:
                DEC += 1
        return [JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]
    return False
