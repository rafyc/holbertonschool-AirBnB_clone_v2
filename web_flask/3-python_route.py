#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    '''
    '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''
    '''
    return "<p>HBNB</p>"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    '''
    '''
    return f'C {text.replace("_", " ")}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    '''
    '''
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
