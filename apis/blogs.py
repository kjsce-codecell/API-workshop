from flask import Blueprint, request, jsonify, render_template
import os
import random
import json
import datetime

blogs = Blueprint('blogs', __name__)


@blogs.route('/random')
def random_blog():
    all_blogs = os.listdir('apis/data/blogs/')
    r = random.randint(0, len(all_blogs)-1)
    blog = all_blogs[r]
    with open('apis/data/blogs/' + blog, 'r') as f:
        data = json.load(f)
    
    return jsonify(data)


@blogs.route('/blog')
def get_blog_by_tags():
    tags = request.args.get('tags')
    all_blogs = os.listdir('apis/data/blogs/')
    print("tags", tags)
    result = []
    for blog in all_blogs:
        with open('apis/data/blogs/' + blog, 'r') as f:
            data = json.load(f)
        print("array", data['tags'])
        data_array = data['tags']
        if (tags in data_array):
            result.append(data)
    
    return jsonify(result)

@blogs.route('/docs')
def docs():
    endpoints = [
        {
            'url': '/random',
            'method': 'GET',
            'description': 'Fetch json of any random blog. \n Example: blogs/random'
        },
        {
            'url': '/blog',
            'method': 'GET',
            'description': 'Fetch blogs with a particular tag. \n Example: blogs/blog?tags=Science'
        },
    ]

    return jsonify({'endpoints': endpoints})
