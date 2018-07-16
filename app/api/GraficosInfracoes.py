from flask import render_template
from app import app
from app.controllers.PesquisaForms import pesquisaForm
from app.controllers.ControleRegistroInfracaoCSV import getTodosRegistrosDeInfracoes

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = []

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/infracoesgraficos')
def graficos_infracoes():
    bar_labels = labels
    bar_values = []
    form = pesquisaForm()
    if form.validate_on_submit():
        bar_values = getTodosRegistrosDeInfracoes(form.buscaBairro.data)

    return render_template('graficos_infracoes.html', title='Grafico de Infracoes', max=17000, labels=bar_labels,
                           values=bar_values, set=zip(values, labels, colors), form=form)