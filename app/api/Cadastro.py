from flask import render_template, redirect, url_for
from app import app
from app.models.UsuarioObjeto import usuario
from app.models.EntidadeObjeto import entidade
from app.controllers.CadastroForms import CadastroForm
from app.controllers.UserControllers import valida_user, inserirUser, getIdMax
from app.models.EnderecoObjetoEntidade import enderecoEntidade
from app.controllers.ControleEnderecoEntidade import getIdMax, inserirEnderecoEntidade

@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        objUser = usuario(form.mail.data, form.password.data)
        objEnderecoEntidade = enderecoEntidade(form.rua.data, form.bairro.data, form.cidade.data,
                                               form.estado.data, form.numero.data, form.cep.data)
        id_user_maximo = getIdMax(objUser) + 1
        id_endereco_maximo = getIdMax(objEnderecoEntidade) + 1
        print(id_endereco_maximo)
        objUser.setId(id_user_maximo)
        objEnderecoEntidade.setId(id_endereco_maximo)
        objEntidade = entidade(None, form.cnpj.data, None, form.telefone.data, form.tipo_entidade.data,
                               form.razao_social.data, id_endereco_maximo,
                               id_user_maximo)

        if valida_user(objUser) == False:
            inserirEnderecoEntidade(objEnderecoEntidade)
            inserirUser(objUser, objEntidade)
            print('Usuario cadastrado com sucesso!')
            return redirect(url_for('tela_principal'))
            # return redirect(url_for('tela_principal'))
        print('Usuario não cadastrado!')
    return render_template('cadastro.html', form=form)

