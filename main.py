import psycopg2
from flask import Flask, request, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
import db
from forms import LibrosForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 's8p3rs3cret0'

@app.route('/')
def index():
    return render_template('base.html')

@app.errorhandler(404)
def error404(error):
    return render_template('404.html')

@app.route('/libros')
def libros():
    conn= db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    #Ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM libros_view''')
    #Recuperar información
    datos = cursor.fetchall()
    #Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('libros.html', datos=datos)

@app.route('/insertar_libro', methods=['GET', 'POST'])
def insertar_libro():
    form = LibrosForm()
    if form.validate_on_submit():
        #Si se dio click en el botón del formulario y no faltan datos
        #Se recupera la información que el user escribió en el form
        titulo = form.titulo.data
        fk_autor = form.fk_autor.data
        fk_editorial = form.fk_editorial.data
        edicion = form.edicion.data
        #Insertar los datos
        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO libro (titulo, fk_autor, fk_editorial, edicion)
                       VALUES (%s, %s, %s, %s)
        ''', (titulo, fk_autor, fk_editorial, edicion))
        conn.commit()
        cursor.close()
        db.desconectar()
        return redirect(url_for('libros'))
    return render_template('insertar_libro.html', form=form)


@app.route('/autores')
def autores():
    conn= db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    #Ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM autores_view''')
    #Recuperar información
    datos = cursor.fetchall()
    #Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('autores.html', datos=datos)

@app.route('/paises')
def pais():
    conn= db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    #Ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM pais ORDER BY idpais''')
    #Recuperar información
    datos = cursor.fetchall()
    #Cerrar cursor y conexión a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('paises.html', datos=datos)

@app.route('/delete_pais/<int:idpais>', methods=['POST'])
def delete_pais(idpais):
    conn= db.conectar()
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    #Borrar el registro con el id_pasi seleccionado
    cursor.execute('DELETE FROM pais WHERE idpais=%s', (idpais,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for ('index'))

@app.route('/update1_pais/<int:idpais>', methods=['POST'])
def update1_pais(idpais):
    conn= db.conectar()
    # crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    # recuperar el registro del id_pais seleccionado
    cursor.execute('''SELECT * FROM pais WHERE idpais=%s''',
                   (idpais,))
    datos= cursor.fetchall()
    cursor.close()
    db.desconectar(conn)
    return render_template ('editar_pais.html', datos=datos)

@app.route('/update2_pais/<int:idpais>', methods=['POST'])
def update2_pais(idpais):
    nombrepais = request.form['nombre']  # Obtener el valor del campo 'nombre' del formulario
    conn= db.conectar()
    cursor = conn.cursor()
    cursor.execute('''UPDATE pais SET nombrepais=%s WHERE idpais=%s''', (nombrepais, idpais,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))
