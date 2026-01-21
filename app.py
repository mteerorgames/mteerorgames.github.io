from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__)
CARPETA = 'archivos'
os.makedirs(CARPETA, exist_ok=True)

@app.route('/')
def inicio():
    return open('index.html').read()

@app.route('/subir', methods=['POST'])
def subir():
    archivo = request.files['archivo']
    archivo.save(os.path.join(CARPETA, archivo.filename))
    return 'Archivo subido. <a href="/">Volver</a>'

@app.route('/archivos/<nombre>')
def descargar(nombre):
    return send_from_directory(CARPETA, nombre, as_attachment=True)

@app.route('/archivos')
def listar():
    return jsonify(os.listdir(CARPETA))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
