from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NumeroForm(FlaskForm):
    numero_telephone = StringField('Numéro de téléphone', validators=[DataRequired()])
    submit = SubmitField('Convertir')
