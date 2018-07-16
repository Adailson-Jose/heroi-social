from flask import render_template
from app import app
from app.controllers.PesquisaForms import pesquisaForm

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

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/graficosacidentes', methods=["GET", "POST"])
def graficos_acidentes():
    bar_labels = labels
    bar_values = values
    form = pesquisaForm()
    if form.validate_on_submit():
        pass

    return render_template('graficos_acidentes.html', title='Grafico de Acidentes', max=17000, labels=bar_labels,
                  values=bar_values, set=zip(values, labels, colors))