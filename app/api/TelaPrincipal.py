from flask import render_template
from app import app


@app.route('/tela_principal')
@app.route('/')
def index():
    return render_template('tela_principal.html')
