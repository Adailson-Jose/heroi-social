from flask import render_template, redirect, url_for, flash
from app import app
from app.controllers.UserControllers import valida_user
from app.models.UsuarioObjeto import usuario
from app.controllers.PagamentoForms import PagamentoForm


@app.route('/pagamento', methods=["GET", "POST"])
def pagamento():
    form = PagamentoForm()
    if form.validate_on_submit():
        objUser = usuario(form.mail.data, form.password.data)
        if valida_user(objUser):
            print('Logado com sucesso.')
            flash('Verificado com sucesso.')
            return redirect(url_for('boleto'))
        print('Login inválido.')
        flash('E-mail ou senha errada.', 'erro')
    return render_template('pagamento.html', form=form)
