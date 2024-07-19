from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class LibrosForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    fk_autor = IntegerField('Autor ID', validators=[DataRequired()])
    fk_editorial = IntegerField('Editorial ID', validators=[DataRequired()])
    edicion = IntegerField('Edición', validators=[DataRequired()])
    submit = SubmitField('Agregar Libro')