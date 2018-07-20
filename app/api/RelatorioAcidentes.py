from flask import render_template
from app import app
from app.controllers.PesquisaForms import pesquisaForm

@app.route('/relatorio_acidentes', methods=["GET", "POST"])
def relatorio_acidentes():
    form = pesquisaForm()
    if form.validate_on_submit():
        pass

    return render_template('relatorio_acidentes.html', title='Relatório de Acidentes', form = form)