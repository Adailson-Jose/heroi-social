from flask import render_template, redirect, url_for
from app import app
from app.controllers.ContatoForms import ContatoForm


@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('contato.html', form=form)
