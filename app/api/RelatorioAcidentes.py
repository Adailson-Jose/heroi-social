from flask import render_template, request
from app import app
from app.controllers.ControleAcidentesCSV import getTodosAcidentesFiltro2, getBairrosMaisAcidentes
from app.controllers.ControleRelatorioAcidentes import getPercentualAcidenteBairro

@app.route('/relatorio_acidentes', methods=["GET", "POST"])
def relatorio_acidentes():
    listagemPercentual = getPercentualAcidenteBairro()
    comp_select_ano = request.form.get('comp_select_ano')
    comp_select_mes = request.form.get('comp_select_mes')
    comp_select_bairro = request.form.get('comp_select_bairro')
    comp_select_qtd_vitimas = request.form.get('comp_select_qtd_vitimas')
    qtdAcidentes = 0
    automovel = 0
    pedestre = 0
    ciclomotor = 0
    ciclista = 0
    motocicleta = 0
    outros = 0
    choque = 0
    choqueCiclista = 0
    atropelamento = 0
    acidentePercurso = 0
    riscoMaisAlto = [listagemPercentual[0], listagemPercentual[1], listagemPercentual[2]]
    riscoAlto = [listagemPercentual[3], listagemPercentual[4], listagemPercentual[5]]
    riscoMedio = [listagemPercentual[6], listagemPercentual[7], listagemPercentual[8]]
    riscoBaixo = [listagemPercentual[9], listagemPercentual[10], listagemPercentual[11]]
    if comp_select_ano != '' and comp_select_mes !='' and comp_select_bairro !=''and comp_select_qtd_vitimas !='':
        qtdAcidentes = getTodosAcidentesFiltro2(comp_select_ano, comp_select_mes, comp_select_bairro,
                                               comp_select_qtd_vitimas)

    return render_template('relatorio_acidentes.html', title='Relatório de Acidentes', totalDeAcidentes=qtdAcidentes,
                           automovel=automovel,
                           pedestre=pedestre, ciclomotor=ciclomotor, ciclista=ciclista, motocicleta=motocicleta,
                           outros=outros, choque=choque,
                           choqueCiclista=choqueCiclista, atropelamento=atropelamento,
                           acidentePercurso=acidentePercurso, riscoMaisAlto=riscoMaisAlto,
                           riscoAlto=riscoAlto, riscoMedio=riscoMedio, riscoBaixo=riscoBaixo)
