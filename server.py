from flask import Flask, send_file

app = Flask(__name__)

# Ruta principal para evitar 404 en Render
@app.route('/')
def index():
    return "Servidor OTA funcionando 🎉"

# Ruta que sirve tu archivo OTA
@app.route('/simple_ota.bin')
def serve_bin():
    return send_file('simple_ota.bin', as_attachment=True)

