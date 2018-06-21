from flask import render_template
from app import app

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]


@app.route('/linha')
def line():
    line_labels = labels
    line_values = values
    return render_template('grafico_linha.html', title='Grafico Linha', max=17000, labels=line_labels,
                           values=line_values)
