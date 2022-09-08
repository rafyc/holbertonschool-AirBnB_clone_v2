#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext

def teardown_db(execption):
    '''
    '''
    storage.close()

@app.route("/states_list", strict_slashes=False)
def state():
    '''
    '''
    list_state = storage.all(State).values()
    return render_template('7-states_list.html', list=list_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
