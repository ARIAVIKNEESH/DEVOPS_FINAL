from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def get_data():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)
