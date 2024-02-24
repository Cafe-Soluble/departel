from flask import render_template, request, redirect, url_for
from app import app
from app.util.helpers import numero_vers_departements
from app.forms import NumeroForm

@app.route('/')
def index():
    form = NumeroForm()

    return render_template('index.html', title='Accueil', form=form)

@app.route('/resultat', methods=['GET', 'POST'])
def resultat():
    form = NumeroForm()
    if form.validate_on_submit():
        numero_telephone = form.numero_telephone.data
        departements = numero_vers_departements(numero_telephone)
        return render_template('resultat.html', departements=departements, numero_telephone=numero_telephone)
    return redirect(url_for('index'))