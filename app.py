# -*- coding: utf-8 -*-

"""
fortune-service
~~~~~~~~~~~~~~

This is a simple web service for random fortunes.
"""

from fortune import get_random_fortune
from flask import Flask, request, jsonify


app = Flask(__name__)
app.debug = True

@app.route('/')
def index():

    d = {
        'resources': {
            '/random': 'A random json-encoded fortune.',
            '/raw': 'A random plain-text fortune.'
        },
        'source': 'https://github.com/kennethreitz/fortune-service'
    }
    return jsonify(d)


@app.route('/random')
def random_fortune():
    fortune = raw_fortune()

    return jsonify({'fortune': fortune})


@app.route('/raw')
def raw_fortune():
    return get_random_fortune('cookies.dat')

if __name__ == '__main__':
    app.run()