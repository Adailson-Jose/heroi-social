from app import app
from flask import render_template, redirect, url_for
from app.controllers.PesquisaForms import pesquisaForm
from app.controllers.ControleMPS import gerarMapadeCalor
from app.controllers.ControleAcidentesCSV import getTodosAcidentesFiltro, getTodosAcidentesSemaforosFiltro



@app.route('/correalacoes', methods=["GET", "POST"])
def gerente_correlacoes():
    form = pesquisaForm()

    if form.validate_on_submit():

        if form.buscaData.data != '' and len(form.buscaData.data) > 3:
            listaCoordenadas = getTodosAcidentesFiltro(form.buscaData.data, 'buscaData')
            if len(listaCoordenadas[0]) != 0:
                print(len(listaCoordenadas[0]))
                gerarMapadeCalor(listaCoordenadas, 'mapa_calor_acidente')
                return redirect(url_for('mapa_acidente_filtro'))
            return render_template('correalacoes.html', form=form)

        elif form.buscaHora.data != '' and len(form.buscaHora.data) > 1:
            listaCoordenadas = getTodosAcidentesFiltro(form.buscaHora.data, 'buscaHora')
            if listaCoordenadas != None:
                gerarMapadeCalor(listaCoordenadas, 'mapa_calor_acidente')
                return redirect(url_for('mapa_acidente_filtro'))
            return render_template('correalacoes.html', form=form)

        elif form.buscaTipoDeOcorrencia.data != '' and len(form.buscaTipoDeOcorrencia.data) > 1:
            listaCoordenadas = getTodosAcidentesFiltro(form.buscaTipoDeOcorrencia.data, 'buscaTipoDeOcorrencia')
            if listaCoordenadas != None:
                gerarMapadeCalor(listaCoordenadas, 'mapa_calor_acidente')
                return redirect(url_for('mapa_acidente_filtro'))
            return render_template('correalacoes.html', form=form)

        elif form.buscaTipo.data != '' and len(form.buscaTipo.data) > 1:
            listaCoordenadas = getTodosAcidentesFiltro(form.buscaTipo.data, 'buscaTipo')
            if listaCoordenadas != None:
                gerarMapadeCalor(listaCoordenadas, 'mapa_calor_acidente')
                return redirect(url_for('mapa_acidente_filtro'))
            return render_template('correalacoes.html', form=form)

        elif form.buscaQtd.data != '' and len(form.buscaQtd.data) > 0:
            listaCoordenadas = getTodosAcidentesFiltro(form.buscaQtd.data, 'buscaQtd')
            if listaCoordenadas != None:
                gerarMapadeCalor(listaCoordenadas, 'mapa_calor_acidente')
                return redirect(url_for('mapa_acidente_filtro'))
            return render_template('correalacoes.html', form=form)

        elif form.buscaLocal.data != '' and len(form.buscaLocal.data) > 0:
            listaCoordenadas = getTodosAcidentesFiltro(form.buscaLocal.data, 'buscaLocal')
            if listaCoordenadas != None:
                gerarMapadeCalor(listaCoordenadas, 'mapa_calor_acidente')
                return redirect(url_for('mapa_acidente_filtro'))
            return render_template('correalacoes.html', form=form)

        elif form.buscaLocalAcidenteSemaforo.data != '' and len(form.buscaLocalAcidenteSemaforo.data) > 0:
            listaCoordenadas = getTodosAcidentesSemaforosFiltro(form.buscaLocalAcidenteSemaforo.data, 'buscaLocalAcidenteSemaforo')
            if listaCoordenadas != None:
                gerarMapadeCalor(listaCoordenadas, 'mapa_calor_acidente')
                return redirect(url_for('mapa_acidente_filtro'))
            return render_template('correalacoes.html', form=form)

    return render_template('correalacoes.html', form=form)
