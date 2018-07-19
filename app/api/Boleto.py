from flask import render_template
from app import app


@app.route('/boleto')
def boleto():
    return render_template('boleto.html')
