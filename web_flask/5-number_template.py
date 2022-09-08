#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    '''
    '''
    return "<p>Hello HBNB!</p>"


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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''
    '''
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    '''
    '''
    return render_template('5-number.html', name=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
