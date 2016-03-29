from flask import jsonify
from flask import request

from . import app


@app.route('/')
def index():
    return jsonify(msg='The Mock API is running...')


@app.route('/webhook-debugger', methods=['POST'])
def debug_webhook():
    data = request.get_json(force=True, silent=True) or request.data
    return jsonify(event=data)
