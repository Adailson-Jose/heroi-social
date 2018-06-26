from flask import render_template
from app import app

bancoDados = [
    ['Lat', 'Long', 'Name'],
    [37.4232, -122.0853, 'Work'],
    [37.4289, -122.1697, 'University'],
    [37.6153, -122.3900, 'Airport'],
    [37.4422, -122.1731, 'Shopping']
    ]
@app.route('/mapa-acidente')
def mapa_acidente():
    return render_template('mapa_acidente.html', title='Mapa de acidentes', set=zip(bancoDados))
