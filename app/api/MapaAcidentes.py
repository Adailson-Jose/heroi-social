from flask import render_template
from app import app
from app.controllers.ControleAcidentesCSV import getTodosAcidentes
from app.controllers.ControleMPS import gerarMapadeCalor


@app.route('/mapa_calor_acidente')
def mapa_acidente():
    coordenadas = getTodosAcidentes()
    gerarMapadeCalor(coordenadas, 'mapa_calor_acidente')
    return render_template('mapa_calor_acidente.html')
