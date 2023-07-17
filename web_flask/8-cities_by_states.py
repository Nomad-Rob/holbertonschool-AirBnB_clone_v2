#!/usr/bin/python3
""" Start a Flask web application """

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


def StartFlask():
    """ Start a Flask web application """
    app.run(host='0.0.0.0', port=5000)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ Display List of States """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states.values())


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    StartFlask()
