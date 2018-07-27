from flask import render_template, request
from app import app
from app.controllers.ControleGraficoAcidente import getTodosAcidenteAno

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/graficosacidentes', methods=["GET", "POST"])
def graficos_acidentes():
    comp_select_ano = request.form.get('comp_select_ano')
    print(comp_select_ano)
    bar_labels = labels
    if comp_select_ano != '':
        bar_values = getTodosAcidenteAno(str(comp_select_ano))
        maximo = max(bar_values)
        print(sum(bar_values))
    return render_template('graficos_acidentes.html', title='Grafico de Acidentes', max=maximo, labels=bar_labels,
                           values=bar_values, set=zip(bar_values, labels, colors))
