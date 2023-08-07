from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

with open('config.json', 'r') as f:
    config = json.load(f)

host = config['SERVER']['host']
port = config['SERVER']['port']

PROCESSED_DATA = []


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/csi-data/', methods=['POST', 'GET'])
def handle_data():
    global PROCESSED_DATA

    if request.method == 'POST':
        csi_data = request.get_json()
        PROCESSED_DATA = csi_data['data']

        print(PROCESSED_DATA)

        return jsonify({"success": True})

    else:
        print(PROCESSED_DATA)
        return render_template('test.html', data=json.dumps(PROCESSED_DATA))


@app.route('/get_data/')
def get_data():
    global PROCESSED_DATA
    return jsonify(data=PROCESSED_DATA)

if __name__ == '__main__':
    app.run(host=host, port=port)
