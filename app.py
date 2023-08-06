from http import HTTPStatus
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('config.json', 'r') as f:
    config = json.load(f)

host = config['SERVER']['host']
port = config['SERVER']['port']


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/csi-data', methods=['POST'])
def post():
    params = request.get_json()
    print(params)
    return jsonify({"data": params, "status": HTTPStatus.OK})


if __name__ == '__main__':
    app.run(host=host, port=port)
