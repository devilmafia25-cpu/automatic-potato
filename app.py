from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/_health')
def health():
    return jsonify({"status": "ok"})

@app.route('/')
def index():
    return jsonify({"message": "Automatic Potato API working fine!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
