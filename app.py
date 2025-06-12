from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

CSV_FILE = 'resultado.csv'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        datos = {
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'email': request.form['email'],
            'password': request.form['password'],
            'edad': request.form['edad'],
            'codigo_postal': request.form['codigo_postal'],
            'estado': request.form['estado']
        }

        archivo_nuevo = not os.path.exists(CSV_FILE)

        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
            escritor = csv.DictWriter(file, fieldnames=datos.keys())

            if archivo_nuevo:
                escritor.writeheader()

            escritor.writerow(datos)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)