from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

# Importar las rutas después de la configuración de la app y la base de datos
from routes import *  # Importa todas las rutas desde routes.py

if __name__ == '__main__':
   with app.app_context():
    db.create_all()
   app.run(debug=True, port=8080)
 






