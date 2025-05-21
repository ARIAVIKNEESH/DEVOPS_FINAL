from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Base URLs of backend microservices (adjust host & ports if needed)
BACKENDS = {
    "student": "http://student-service:5100/",
    "contact": "http://contact-service:5100/",
    "academic": "http://academic-service:5100/",
    "exam": "http://exam-service:5100/",
    "library": "http://library-service:5100/",
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch/<service>')
def fetch_service_data(service):
    url = BACKENDS.get(service)
    if not url:
        return jsonify({"error": "Invalid service name"}), 404
    try:
        resp = requests.get(url, timeout=3)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
