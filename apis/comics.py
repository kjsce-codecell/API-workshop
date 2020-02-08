from flask import Blueprint, request, jsonify, render_template
import os
import random
import json
import datetime

comics = Blueprint('comics', __name__)


@comics.route('/random')
def random_comic():
    is_json = request.args.get('json')
    all_comics = os.listdir('apis/data/comics/')
    r = random.randint(0, len(all_comics)-1)
    comic = all_comics[r]
    with open('apis/data/comics/' + comic, 'r') as f:
        data = json.load(f)
    if is_json is not None:
        return jsonify(data)
    else:
        return render_template('comic.html', artist=data)


@comics.route('/add', methods=["POST"])
def add_comic():
    data = request.get_json()
    name = data.get('title')
    try:
        all_comics = os.listdir('apis/data/comics/')
        if name + '.json' in all_comics:
            return jsonify({"message": "Comic with title:'{}' already exists".format(name)})
        with open('apis/data/comics/{}.json'.format(name), 'w') as f:
            json.dump(data, f)
        return jsonify({"message": "Comic added successfully"})
    except Exception as err:
        return jsonify({"message": "Comic could not be added", "error": err})


@comics.route('/docs')
def docs():
    endpoints = [
        {
            'url': '/random',
            'method': 'GET',
            'description': 'Fetch the html page of a random comic. ' +
                'Use /api/comics/random/?json to the data in json format'
        },
        {
            'url': '/add',
            'method': 'POST',
            'description': 'Send a json containing the comic data having '+
                'the following format: {}'.format({
                "name": "Name",
                "title": "Title of the comic",
                "quote_1": "Quote 1",
                "quote_2": "Quote 2",
                "quote_3": "Quote 3"
            })
        }
    ]

    return jsonify({'endpoints': endpoints})
