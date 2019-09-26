from flask import Flask, jsonify, request
from os import path
from filemanager import open_system_file_manager

app = Flask(__name__)


@app.route('/open', methods=['POST'])
def open_file():
    file_path = request.get_json()['path']
    if path.exists(file_path):
        open_system_file_manager(file_path)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8082)
