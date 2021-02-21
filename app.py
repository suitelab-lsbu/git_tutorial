from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/multiply/<a>/<b>', methods=['GET'])
def multiply(a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return jsonify({'Value Error': "Only numbers Please"})
    return jsonify({'result': a * b})


@app.route('/add/<a>/<b>', methods=['GET'])
def add(a, b):
    return jsonify({'result': f"{a} + {b}"})


@app.route('/subtract/<a>/<b>', methods=['GET'])
def subtract(a, b):
    return jsonify({'result': f"{a} - {b}"})


@app.route('/divide/<a>/<b>', methods=['GET'])
def divide(a, b):
    return jsonify({'result': f"{a} / {b}"})


@app.route('/mod/<a>/<b>', methods=['GET'])
def modulus(a, b):
    return jsonify({'result': f"{a} % {b}"})


if __name__ == '__main__':
    app.run()
