from flask import Blueprint, request, jsonify, render_template
import os
import random
import json
import datetime

tv_shows = Blueprint('tv_shows', __name__)

@tv_shows.route('/random')
def random_tv_show():
    is_json = request.args.get('json')
    all_tv_shows = os.listdir('apis/data/tv_shows/')
    r = random.randint(0, len(all_tv_shows)-1)
    tv_show = all_tv_shows[r]
    with open('apis/data/tv_shows/' + tv_show, 'r') as f:
        data = json.load(f)
        genre = ', '.join(data['genres'])
    if is_json is not None:
        return jsonify(data)
    else:
        return render_template('tv_show.html', tv_show=data, genre=genre)


@tv_shows.route('/docs')
def docs():
    endpoints = [
        {
            'url': '/random',
            'method': 'GET',
            'description': 'Fetch the html page of a random tv shows. ' +
                'Use /api/tv_shows/random?json to the data in json format'
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
