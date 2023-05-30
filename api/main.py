from flask import Flask,  jsonify
from flask_cors import CORS

from .core.core import gold

app = Flask(__name__)
CORS(app)


@app.route('/api/gold', methods=['GET'])
def gold_price():
    g = gold()

    return jsonify(g)
