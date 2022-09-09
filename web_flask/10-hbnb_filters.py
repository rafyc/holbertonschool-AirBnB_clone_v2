#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(execption):
    '''
    '''
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filter():
    '''
    '''
    list_state = storage.all(State).values()
    list_amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', list_state=list_state,
                           liste_amenities=list_amenities)
