#!/usr/bin/python3
'''Starts a Flask web app listening on 0.0.0.0 port 5000'''
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    '''method displays
    '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''method displays
    '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    '''method displays and repace
    '''
    return 'C {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
