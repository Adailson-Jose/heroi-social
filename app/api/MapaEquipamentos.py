from flask import render_template
from app import app
from app.controllers.ControleMPS import gerarMapadePonto
from app.controllers.ControleEquipamentosCSV import getTodosEquipamentos

coordenadas = getTodosEquipamentos()


@app.route('/mapa_equipamentos')
def mapa_equipamentos():
    gerarMapadePonto(coordenadas,'mapa_ponto_equipamentos')
    return render_template('mapa_ponto_equipamentos.html')
