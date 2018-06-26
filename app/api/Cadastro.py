from flask import render_template, redirect, url_for
from app import app
from app.models.UsuarioObjeto import usuario
from app.models.EntidadeObjeto import entidade
from app.controllers.CadastroForms import CadastroForm
from app.controllers.UserControllers import valida_user, inserirUser


@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        objUser = usuario(form.mail.data, form.password.data)
        objEntidade = entidade(None, form.cnpj.data, None, form.telefone.data, form.tipo_entidade.data, None, None,
                               form.razao_social.data)
        if valida_user(objUser) == False:
            inserirUser(objUser, objEntidade)
            print('Usuario cadastrado com sucesso!')
            return redirect(url_for('index'))
        print('Usuario não cadastrado!')
    return render_template('cadastro.html', form=form)
