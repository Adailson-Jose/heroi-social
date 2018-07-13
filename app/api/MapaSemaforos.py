from flask import render_template
from app import app
from app.controllers.ControleMPS import gerarMapadePonto
from app.controllers.ControleSemaforos import getTodosSemaforos

coordenadas = getTodosSemaforos()


@app.route('/mapa_semaforos')
def mapa_semaforos():
    gerarMapadePonto(coordenadas,'mapa_ponto_semaforos')
    return render_template('mapa_ponto_semaforos.html')
