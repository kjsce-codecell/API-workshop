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

@tv_shows.route('/add', methods=["POST"])
def add_tv_show():
    data = request.get_json()
    name = data.get('name')
    try:
        all_tv_shows = os.listdir('apis/data/tv_shows/')
        if name + '.json' in all_tv_shows:
            return jsonify({"message": "Tv show with title:'{}' already exists".format(name)})
        with open('apis/data/tv_shows/{}.json'.format(name), 'w') as f:
            json.dump(data, f)
        return jsonify({"message": "Tv show added successfully"})
    except Exception as err:
        return jsonify({"message": "Tv show could not be added", "error": err})

@tv_shows.route('/tv_show', methods=['GET'])
def get_tv_show():
    imdb_id = request.args.get('id')
    print(imdb_id)
    try:
        all_tv_shows = os.listdir('apis/data/tv_shows/')
        data = []
        for tv_show in all_tv_shows:
            with open('apis/data/tv_shows/' + tv_show, 'r') as f:
                json_data = json.load(f)
                if imdb_id == json_data['imdb_link']:
                    data = json_data
                    break
        return jsonify({ 'data': data })
    except Exception as err:
        return jsonify({"message": "Tv show not found", "error": err})
   
              

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
                "name": "Name of the TV Show",
                "premiered": "Date of the premiere in DD-MM-YYYY",
                "genres": [
                    "Genre 1",
                    "Genre 2",
                ],
                "runtime": "Average runtime (e.g 57min)",
                "no_of_seasons": "integer",
                "imdb_rating": "IMDB rating",
                "imdb_link": "ID of the IMDB page of the tv show"
            })
        },
        {
            'url': '/tv_show',
            'method': 'GET',
            'description': 'Send a json containing the tv show data specified by the id',
            'query_string': 'id = ' + 'the IMDB id'
        }
    ]

    return jsonify({'endpoints': endpoints})
