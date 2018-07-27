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
    lista = [comp_select_ano, comp_select_mes, comp_select_bairro, comp_select_qtd_vitimas]

    riscoMaisAlto = [listagemPercentual[0], listagemPercentual[1], listagemPercentual[2]]
    riscoAlto = [listagemPercentual[3], listagemPercentual[4], listagemPercentual[5]]
    riscoMedio = [listagemPercentual[6], listagemPercentual[7], listagemPercentual[8]]
    riscoBaixo = [listagemPercentual[9], listagemPercentual[10], listagemPercentual[11]]

    cont = 0
    for i in lista:
        if i != None:
            cont += 1
    if cont != 0:
        dadosAcidentes = getTodosAcidentesFiltro2(comp_select_ano, comp_select_mes, comp_select_bairro,
                                                  comp_select_qtd_vitimas)
        if dadosAcidentes:
            return render_template('relatorio_acidentes.html', title='Relatório de Acidentes',
                                   totalDeAcidentes=dadosAcidentes[0], automovel=dadosAcidentes[1],
                                   pedestre=dadosAcidentes[2], ciclomotor=dadosAcidentes[3],
                                   ciclista=dadosAcidentes[4], motocicleta=dadosAcidentes[5],
                                   outros=dadosAcidentes[6], choque=dadosAcidentes[7],
                                   choqueCiclista=dadosAcidentes[8], atropelamento=dadosAcidentes[9],
                                   acidentePercurso=dadosAcidentes[10], outros2=dadosAcidentes[11],
                                   riscoMaisAlto=riscoMaisAlto, riscoAlto=riscoAlto, riscoMedio=riscoMedio,
                                   riscoBaixo=riscoBaixo)

    return render_template('relatorio_acidentes.html', title='Relatório de Acidentes',
                           riscoMaisAlto=riscoMaisAlto, riscoAlto=riscoAlto, riscoMedio=riscoMedio,
                           riscoBaixo=riscoBaixo)
