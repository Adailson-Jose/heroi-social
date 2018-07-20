from flask import render_template
from app import app
from app.controllers.PesquisaForms import pesquisaForm

@app.route('/relatorio_infracoes', methods=["GET", "POST"])
def relatorio_infracoes():
    form = pesquisaForm()
    if form.validate_on_submit():
        pass

    return render_template('relatorio_infracoes.html', title='Relatório de Infrações', form = form)