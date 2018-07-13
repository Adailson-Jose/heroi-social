from flask import render_template
from app import app

coordenadas =[]
ruas =[]

@app.route('/mapa_semaforos')
def mapa_semaforos():
    return render_template('mapa_semaforos_calor.html',title='Mapa de Semaforos', coordenadas=coordenadas, ruas=ruas)
