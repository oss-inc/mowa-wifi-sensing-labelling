from flask import Flask, request, jsonify, render_template
import mysql.connector
import json
import time
from datetime import datetime, timedelta

app = Flask(__name__)

with open('config.json', 'r') as f:
    config = json.load(f)

PROCESSED_DATA = []
table_name = ""


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/create_collection/', methods=['POST'])
def create_table():
    data = request.get_json()

    label = data['label']
    hours = int(data['hours'])
    minutes = int(data['minutes'])
    seconds = int(data['seconds'])

    current_time = datetime.now()
    end_time = current_time + timedelta(hours=hours, minutes=minutes, seconds=seconds)

    current_time_formatted = current_time.strftime('%Y_%m_%d_%H_%M_%S')
    end_time_formatted = end_time.strftime('%Y_%m_%d_%H_%M_%S')

    global table_name

    table_name = f"{label}_{current_time_formatted}_{end_time_formatted}"

    db_connection = mysql.connector.connect(
        host=config['Database']['host'],
        user=config['Database']['user'],
        password=config['Database']['password'],
        database=config['Database']['database']
    )

    cursor = db_connection.cursor()

    columns = [f"sub_{i} DOUBLE" for i in range(64)]
    columns_query = ", ".join(columns)

    create_table_query = f"""
    CREATE TABLE mowa.{table_name} (
        {columns_query}
    );
    """

    cursor.execute(create_table_query)
    db_connection.commit()
    cursor.close()

    return jsonify({"success": True})


@app.route('/insert_data/', methods=['POST'])
def start_collection():
    try:
        global table_name

        data = request.json  # 클라이언트로부터 전송된 JSON 데이터

        db_connection = mysql.connector.connect(
            host=config['Database']['host'],
            user=config['Database']['user'],
            password=config['Database']['password'],
            database=config['Database']['database']
        )

        cursor = db_connection.cursor()

        # 컬럼명을 쿼리에 포함시키는 부분
        columns = [f"sub_{i}" for i in range(64)]  # 데이터의 개수에 맞게 컬럼 이름 생성
        columns_str = ', '.join(columns)

        # 데이터 값을 쿼리에 포맷하여 넣어주는 부분
        values_str = ', '.join(str(value) for value in data)
        # print(columns_str)
        # print(values_str)

        # print(table_name)
        insert_data_query = f"INSERT INTO mowa.{table_name} ({columns_str}) VALUES ({values_str});"

        cursor.execute(insert_data_query)

        db_connection.commit()

        cursor.close()

        return jsonify({"success": True})

    except Exception as e:
        # print(e)
        return jsonify({"success": False, "error": str(e)})


@app.route('/end_collection/', methods=['POST'])
def end_collection():
    try:
        global table_name

        db_connection = mysql.connector.connect(
            host=config['Database']['host'],
            user=config['Database']['user'],
            password=config['Database']['password'],
            database=config['Database']['database']
        )

        cursor = db_connection.cursor()

        current_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

        global table_name
        prefix, timestamp, _, _, _, _, _ = table_name.rsplit('_', 6)

        new_table_name = f"{prefix}_{current_time}"

        if new_table_name != table_name:
            rename_query = f"RENAME TABLE {table_name} TO {new_table_name};"
            cursor.execute(rename_query)
            db_connection.commit()

        cursor.close()

        return jsonify({"success": True})

    except Exception as e:
        # print(e)
        return jsonify({"success": False, "error": str(e)})


@app.route('/get_config/')
def get_config():
    return jsonify(config=config['SERVER']['host'])


@app.route('/csi-data/', methods=['POST', 'GET'])
def handle_data():
    global PROCESSED_DATA

    if request.method == 'POST':
        csi_data = request.get_json()
        PROCESSED_DATA = csi_data['data']

        # print(PROCESSED_DATA)

        return jsonify({"success": True})

    else:
        # print(PROCESSED_DATA)
        return render_template('index.html', data=json.dumps(PROCESSED_DATA))


@app.route('/get_data/')
def get_data():
    global PROCESSED_DATA
    return jsonify(data=PROCESSED_DATA)


if __name__ == '__main__':
    app.run(host=config['SERVER']['host'], port=config['SERVER']['port'])
