from flask import render_template, request
from app import app
from app.controllers.ControleAcidentesCSV import getTodosAcidentesFiltro2

@app.route('/relatorio_acidentes', methods=["GET", "POST"])
def relatorio_acidentes():
    comp_select_ano = request.form.get('comp_select_ano')
    comp_select_mes = request.form.get('comp_select_mes')
    comp_select_bairro = request.form.get('comp_select_bairro')
    comp_select_qtd_vitimas = request.form.get('comp_select_qtd_vitimas')
    qtdAcidentes = 0
    if comp_select_ano != '' and comp_select_mes !='' and comp_select_bairro !=''and comp_select_qtd_vitimas !='':
        qtdAcidentes = getTodosAcidentesFiltro2(comp_select_ano, comp_select_mes, comp_select_bairro,
                                               comp_select_qtd_vitimas)

    return render_template('relatorio_acidentes.html', title='Relatório de Acidentes', totalDeAcidentes=qtdAcidentes)