from flask import Flask, send_file

app = Flask(__name__)

@app.route('/simple_ota.bin')
def serve_bin():
    return send_file('simple_ota.bin', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
