# Départel

Départel est une application web Flask qui convertit les numéros de téléphone en listes de départements français.

Démo : [www.departel.fr](https://departel.fr)

## Téléchargement

Cloner le repository : 
```git
git clone https://github.com/Cafe-Soluble/departel.git
cd Departel
```

## Configuration de l'environnement

1. Installer Python 3 si pas déjà installé.
2. Créer un environnement virtuel : `python3 -m venv venv`
3. Activer l'environnement :
   - Sous Windows : `venv\Scripts\activate`
   - Sous Unix ou MacOS : `source venv/bin/activate`
4. Installer les dépendances : `pip install -r requirements.txt`

## Lancer l'application

1. Définir la variable d'environnement :
   - Sous Windows : `set FLASK_APP=run.py`
   - Sous Unix ou MacOS : `export FLASK_APP=run.py`
2. Lancer l'application : `flask run`
3. Ouvrir un navigateur et aller à `http://127.0.0.1:5000/`

## Contribution

Pour contribuer au projet, veuillez créer une branche et soumettre une pull request pour toute proposition de modification.
