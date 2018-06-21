from flask import render_template
from app import app


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')
