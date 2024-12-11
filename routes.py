from app import app, db
from models import Usuario  # Asegúrate de que tienes un modelo Usuario correctamente definido
from flask import render_template, redirect, url_for

# Ruta para agregar un usuario
@app.route('/add_user/<nombre>/<email>')
def add_user(nombre, email):
    usuario = Usuario(nombre=nombre, email=email)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('usuarios'))

# Ruta para ver todos los usuarios
@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)




