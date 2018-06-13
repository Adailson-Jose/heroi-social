from flask import render_template
from app import app, db
from app.models.tabelas import usuario


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('login.html')

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
    i = usuario('Adailson@gmail', 12345)
    db.session.add(i)
    db.session.commit()
    return 'OKKKKK'


@app.route('/teste/listar', defaults={'info': None})
def testeListarar(info):
    r = usuario.query.filter_by(email='Adailson@gmail').all()
    print(r)
    return 'okkk'


@app.route('/teste/', defaults={'info': None})
def testeListarar(info):
    r = usuario.query.filter_by(email='Adailson@gmail').all()
    print(r)
    return 'okkk'
