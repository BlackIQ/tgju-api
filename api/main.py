from flask import Flask,  jsonify
from flask_cors import CORS

from .core.core import gold, currency

app = Flask(__name__)
CORS(app)


@app.route('/api/gold', methods=['GET'])
def gold_price():
    g = gold()

    return jsonify(g), 200


@app.route('/api/currency', methods=['GET'])
def currency_price():
    c = currency()

    return jsonify(c), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Route not found'}), 404
