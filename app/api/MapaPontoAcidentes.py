from flask import render_template
from app import app
from app.controllers.ControleAcidentesCSV import getTodosAcidentes
from app.controllers.ControleMPS import gerarMapadePonto

coordenadas =getTodosAcidentes()

@app.route('/mapa_pontos_acidente')
def mapa_ponto_acidente():
    gerarMapadePonto(coordenadas, 'mapa_ponto_acidente')
    return render_template('mapa_ponto_acidente.html')
