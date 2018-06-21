from flask import render_template
from app import app


@app.route('/principal')
def principal():
    return render_template('principal.html')
