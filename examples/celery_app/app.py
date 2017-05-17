from flask import Flask, jsonify
from flask_cors import CORS

import tasks

app = Flask(__name__)
# Allow any origin
CORS(app)


@app.route('/')
def index():
    return 'Its working!'


@app.route('/add/<int:x>/<int:y>', methods=['POST'])
def add(x, y):
    task = tasks.add.delay(x, y)
    return jsonify({'task_id': task.id})


if __name__ == '__main__':
    app.run()
