from flask import render_template, flash, redirect, url_for
from app import app, db, lm
from app.controllers.Logar import Logar
from app.models.Tabelas import usuario, entidade, endereco
from app.controllers.LoginForms import LoginForm
from app.controllers.CadastroForms import CadastroForm
from app.controllers.ContatoForms import ContatoForm
from flask_login import logout_user
from app.controllers.InserirObjetos import InserirObjetos

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/principal')
def principal():
    return render_template('principal.html')


@lm.user_loader
def load_user(id):
    print(usuario.email)
    return usuario.query.filter_by(id=usuario.id).first()

@app.route('/login', methods=["GET", "POST"])
def login():
    logar = Logar()
    form = LoginForm()
    if form.validate_on_submit():
        objUser = usuario(form.mail.data, form.password.data)
        if logar.logar(objUser):
            print('Logado com sucesso.')
            return redirect(url_for('principal'))
        print('Login inválido.')
    return render_template('login.html', form=form)


@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    criarUser = InserirObjetos()
    if form.validate_on_submit():
        objUser = usuario(form.mail.data, form.password.data)
        objEntidade = entidade(None, form.cnpj.data, None, form.telefone.data, form.tipo_entidade.data, None, None,
                               form.razao_social.data)
        if criarUser.inserirUser(objUser, objEntidade):
            print('Usuario cadastrado com sucesso!')
            return redirect(url_for('index'))
        print('Usuario não cadastrado!')
    return render_template('cadastro.html', form=form)


@app.route('/sair')
def sair():
    logout_user()
    flash('Saindo da aplicação.')
    return redirect(url_for('index'))


@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('contato.html', form=form)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/teste/criar', defaults={'info': None})
def testeCriar(info):
    i = usuario('Adailson@gmail.com', 12345)
    db.session.add(i)
    db.session.commit()
    return 'OKKKKK'


@app.route('/teste/', defaults={'info': None})
def testeListarar(info):
    r = usuario.query.filter_by(email='Adailson@gmail.com').first()
    print(r)
    return


# Rotas para gráficos

@app.route('/pizza')
def grafico_pizza():
    pie_labels = labels
    pie_values = values
    return render_template('grafico_pizza.html', title='Grafico Pizza', max=17000, set=zip(values, labels, colors))


@app.route('/barras')
def grafico_barra():
    bar_labels = labels
    bar_values = values
    return render_template('grafico_barras.html', title='Grafico de Barras', max=17000, labels=bar_labels,
                           values=bar_values)


@app.route('/linha')
def line():
    line_labels = labels
    line_values = values
    return render_template('grafico_linha.html', title='Grafico Linha', max=17000, labels=line_labels,
                           values=line_values)

"""@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = usuario("jadeil@hotmail.com", "5678")
    db.session.add(i)
    db.session.commit()
    return "OK"

@app.route("/teste2/<info>")
@app.route("/teste2", defaults={"info": None})
def teste2(info):
    #r = usuario.query.filter_by(email="jadeil@hotmail.com").all()
    r = usuario.query.filter_by(id="1").all()
    y = usuario.query.filter_by(password="1234").all()
    z = usuario.query.filter_by(email="jadeil@hotmail.com").first()
    print(r)
    print(r.email)
    print(y)
    return "OKKK" """
