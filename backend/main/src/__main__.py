from flask import Flask, jsonify, request

# creating the Flask application
app = Flask(__name__)

@app.route('/response')
def get_response():
    return jsonify('res')