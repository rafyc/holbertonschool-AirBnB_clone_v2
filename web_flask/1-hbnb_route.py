#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "<p>HBNB</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)