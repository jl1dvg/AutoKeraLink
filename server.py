# server.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Aquí se almacenarán temporalmente los datos recibidos
latest_data = {}

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(latest_data)

@app.route('/data', methods=['POST'])
def update_data():
    global latest_data
    latest_data = request.json
    return jsonify({"status": "success"}), 200

def run_server():
    app.run(port=5000)
