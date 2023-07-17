#!/usr/bin/python3
""" Start a Flask web application """

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


def StartFlask():
    """ Start a Flask web application """
    app.run(host='0.0.0.0', port=5000)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Display a message so we know it's running """
    return "Hello World!"


@app.route('/hbnb_filters', strict_slashes=False)
def show_page():
    """ Display List of States """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states.values(), amenities=amenities.values())


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    StartFlask()
