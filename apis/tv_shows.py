from flask import Blueprint, request, jsonify, render_template
import os
import random
import json
import datetime

tv_shows = Blueprint('tv_shows', __name__)

# Get random TV Show
@tv_shows.route('/random')
def random_tv_show():
    # Check if it is a API call
    is_json = request.args.get('json')

    # Get all the tv shows in tv_shows directory
    all_tv_shows = os.listdir('apis/data/tv_shows/')

    # Generate random integer between no. of tv shows
    r = random.randint(0, len(all_tv_shows)-1)

    # Select the tv show
    tv_show = all_tv_shows[r]

    # Load the data of the tv show
    with open('apis/data/tv_shows/' + tv_show, 'r') as f:
        data = json.load(f)
        genre = ', '.join(data['genres'])

    # If it is an API call, return data in json format else render the template
    if is_json is not None:
        return jsonify(data)
    else:
        return render_template('tv_show.html', tv_show=data, genre=genre)


# Add a TV show
@tv_shows.route('/add', methods=["POST"])
def add_tv_show():
    data = request.get_json() # Get the data from the request
    name = data.get('name') # Select the name
    try:
        all_tv_shows = os.listdir('apis/data/tv_shows/') # Select all the TV shows

        # Check if the TV show already exists
        if name + '.json' in all_tv_shows:
            return jsonify({"message": "Tv show with title:'{}' already exists".format(name)})

        # Create a new TV show file
        with open('apis/data/tv_shows/{}.json'.format(name), 'w') as f:
            json.dump(data, f)
        return jsonify({"message": "Tv show added successfully"})
    except Exception as err:
        return jsonify({"message": "Tv show could not be added", "error": err})

# Select the tv_show from imdb_id
@tv_shows.route('/tv_show', methods=['GET'])
def get_tv_show():
    imdb_id = request.args.get('id') # Get the imdb id from the request
    # print(imdb_id)
    try:
        # Select all the tv shows
        all_tv_shows = os.listdir('apis/data/tv_shows/')
        data = []

        # Check if the tv show exists
        for tv_show in all_tv_shows:
            with open('apis/data/tv_shows/' + tv_show, 'r') as f:
                json_data = json.load(f)
                if imdb_id == json_data['imdb_link']:
                    # Found, then select the data and break
                    data = json_data
                    break
        # Return data in json format
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
