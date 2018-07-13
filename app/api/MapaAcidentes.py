from flask import render_template
from app import app
'''from app.controllers.ControleCSV import getEqupamentos'''

coordenadas =[]
ruas =[]

'''listaEquipamentos  = getEqupamentos()

for i in listaEquipamentos:
    localizacao= i.localizacao
    ruas.append(localizacao)
    latitude = float(i.latitude)
    longitude = float(i.longitude)
    lista = [latitude, longitude]
    coordenadas.append(lista)
    print(lista)'''
#print(coordenadas)

@app.route('/mapa-acidentes')
def mapa_acidente():
    return render_template('mapa_acidentes.html', title='Mapa de Acidentes', coordenadas=coordenadas, ruas=ruas)
