from flask import Blueprint, request, jsonify, render_template
import os
import random
import json
import datetime
import praw
import random


memes = Blueprint('memes', __name__)

@memes.route('/random')
def random_meme():
    is_json = request.args.get('json')
    l=[]
    reddit = praw.Reddit(client_id='7jRJOObwgVtOtQ', client_secret='0e2DEos7XwVIAtD4oYKZkL8Zzhw', user_agent='vs')
    mr = reddit.subreddit('memes')
    for post in mr.hot(limit=10):
        l.append(post.url)
    
    r=random.randint(1,9)
    data={'link':''+l[r]}
    if is_json is not None:
        return jsonify(data)
    else:
        # return render_template('memes.html', args here)
        return data

# @memes.route('/add', methods=["POST"])
# def add_tv_show():
#     data = request.get_json()
#     name = data.get('name')
#     try:
#         all_tv_shows = os.listdir('apis/data/tv_shows/')
#         if name + '.json' in all_tv_shows:
#             return jsonify({"message": "Tv show with title:'{}' already exists".format(name)})
#         with open('apis/data/tv_shows/{}.json'.format(name), 'w') as f:
#             json.dump(data, f)
#         return jsonify({"message": "Tv show added successfully"})
#     except Exception as err:
#         return jsonify({"message": "Tv show could not be added", "error": err})

# @memes.route('/wholesome', methods=['GET'])
# def get_tv_show():
#     imdb_id = request.args.get('id')
#     print(imdb_id)
#     try:
#         all_tv_shows = os.listdir('apis/data/tv_shows/')
#         data = []
#         for tv_show in all_tv_shows:
#             with open('apis/data/tv_shows/' + tv_show, 'r') as f:
#                 json_data = json.load(f)
#                 if imdb_id == json_data['imdb_link']:
#                     data = json_data
#                     break
#         return jsonify({ 'data': data })
#     except Exception as err:
#         return jsonify({"message": "Tv show not found", "error": err})



@memes.route('/docs')
def docs():
    endpoints = [
        {
            'url': '/random',
            'method': 'GET',
            'description': 'Get a random meme from the internet! ' +
                'Use /api/memes/random?json to the data in json format'
        },
        {
            'url': '/add',
            'method': 'POST',
            'description': 'Send a json containing the link to a meme having '+
                'the following format: {}'.format({
                "author": "author name",
                "category": "category of the meme wholesome/programming/dank",
                "link": "link to the meme"
            })
        },
        {
            'url': '/wholesome',
            'method': 'GET',
            'description': 'Get a random wholesome meme',
        },
        {
            'url': '/programming',
            'method': 'GET',
            'description': 'Get a random dank meme',
        }
    ]

    return jsonify({'endpoints': endpoints})