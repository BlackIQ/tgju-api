from flask import Flask, request, jsonify
from flask_cors import CORS

from .core.core import gold, currency

app = Flask(__name__)
CORS(app)


@app.route('/api/price/<of>', methods=['GET'])
def get_price(of):
    assert of == request.view_args['of']

    match of:
        case 'gold':
            return jsonify(gold()), 200
        case 'currency':
            return jsonify(currency()), 200
        case _:
            return jsonify({'message': 'Invalid'}), 404


@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Route not found'}), 404
