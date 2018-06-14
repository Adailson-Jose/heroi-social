from flask import render_template, flash, redirect, url_for, request
from app import app, db, lm
from app.models.tabelas import usuario
from app.models.forms import LoginForm
from flask_login import login_user, logout_user, login_manager


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
def load_user(email):
    return usuario.query.filter_by(email=email).first()


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = usuario.query.filter_by(email=form.mail.data).first()
        if user and user.password == form.password.data:
            print(user)
            login_user(user)
            flash('Logado com sucesso.')
            return redirect(url_for('principal'))
        flash('Login inválido.')
    print(form.errors)
    return render_template('login.html', form=form)


"""
@app.route('/login', methods= ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.mail.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html',
                           form=form)

"""

@app.route('/sair')
def sair():
    logout_user()
    flash('Saindo da aplicação.')
    return redirect(url_for('index'))


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/teste/criar', defaults={'info': None})
def testeCriar(info):
    i = usuario('Adailson@gmail.com', 12345)
    db.session.add(i)
    db.session.commit()
    return 'OKKKKK'


'''@app.route('/teste/listar', defaults={'info': None})
def testeListarar(info):
    r = usuario.query.filter_by(email='Adailson@gmail.com').all()
    print(r)
    return 'okkk'
'''


@app.route('/teste/', defaults={'info': None})
def testeListarar(info):
    r = usuario.query.filter_by(email='Adailson@gmail').all()
    print(r)
    return 'okkk'


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
