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
        raw_number = request.form['numero_telephone']
        # Nettoie le numéro en enlevant tous les espaces
        clean_number = raw_number.replace(' ', '')
        departements = numero_vers_departements(clean_number)
        return render_template('resultat.html', departements=departements, numero_telephone=numero_telephone)
    return redirect(url_for('index'))



@app.route('/some_route', methods=['POST'])
def some_function():
    # Supposons que 'numero_telephone' est le nom du champ dans votre formulaire
    raw_number = request.form['numero_telephone']
    # Nettoie le numéro en enlevant tous les espaces
    clean_number = raw_number.replace(' ', '')
    
    # Utilisez `clean_number` pour vos traitements ultérieurs
