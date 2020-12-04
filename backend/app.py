from json import load
from random import shuffle

from flask import Flask
from flask_cors import CORS

with open('burst.json', 'r') as f:
    data = load(f)
    shuffle(data)

with open('unsplash.json', 'r') as f:
    data += load(f)
    shuffle(data)

app = Flask(__name__)
CORS(app)


def get_page(data, page):
    """Get nth page of a data, with each page having 20 entries."""
    begin = page * 20
    end = page * 20 + 20
    if begin >= len(data):
        return []
    elif end >= len(data):
        return data[begin:]
    else:
        return data[begin:end]


@app.route('/all/<int:page>')
def get_all(page):
    """Get a page of 20 images from all sources."""
    return {'data': get_page(data, page)}
