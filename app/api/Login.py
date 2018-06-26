from flask import render_template, redirect, url_for
from app import app
from app.controllers.UserControllers import valida_user
from app.models.UsuarioObjeto import usuario
from app.controllers.LoginForms import LoginForm


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        objUser = usuario(form.mail.data, form.password.data)
        if valida_user(objUser):
            print('Logado com sucesso.')
            return redirect(url_for('principal'))
        print('Login inválido.')
    return render_template('login.html', form=form)
