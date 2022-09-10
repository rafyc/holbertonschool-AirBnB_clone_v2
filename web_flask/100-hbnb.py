#!/usr/bin/python3
'''Starts a Flask web app listening on 0.0.0.0 port 5000'''
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(execption):
    '''
    '''
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''
    '''
    list_user = storage.all(User).values()
    list_place = storage.all(Place).values()
    list_state = storage.all(State).values()
    list_amenities = storage.all(Amenity).values()
    return render_template('100-hbnb.html', list_state=list_state,
                           list_amenities=list_amenities,
                           list_place=list_place, list_user=list_user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
