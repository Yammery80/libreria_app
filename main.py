import psycopg2
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/libros')
def libros():
    #Conectar con DB(DataBase)
    conexion = psycopg2.connect(
        database="biblioteca",
        user="postgres",
        password="Lindel2005",
        host="localhost",
        port="5432"
    )
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    #Ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM libros_view''')
    #Recuperar información
    datos = cursor.fetchall()
    #Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)

@app.route('/autores')
def autores():
    #Conectar con DB(DataBase)
    conexion = psycopg2.connect(
        database="biblioteca",
        user="postgres",
        password="Lindel2005",
        host="localhost",
        port="5432"
    )
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    #Ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM autores_view''')
    #Recuperar información
    datos = cursor.fetchall()
    #Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('autores.html', datos=datos)

@app.route('/pais')
def pais():
    #Conectar con DB(DataBase)
    conexion = psycopg2.connect(
        database="biblioteca",
        user="postgres",
        password="Lindel2005",
        host="localhost",
        port="5432"
    )
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    #Ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM pais''')
    #Recuperar información
    datos = cursor.fetchall()
    #Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('paises.html', datos=datos)
