from flask import render_template
from app import app


@app.route('/mapa_calor_acidente_filtro')
def mapa_acidente_filtro():
    return render_template('mapa_calor_acidente.html')
