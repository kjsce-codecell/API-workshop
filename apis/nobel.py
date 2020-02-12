from flask import Blueprint, request, jsonify, render_template
import os
import random
import json
import datetime

nobel = Blueprint('nobel', __name__)


@nobel.route('/random')
def random_nobel():
	all_nobel = os.listdir('apis/data/nobel/')
	r = random.randint(0, len(all_nobel)-1)
	nobel = all_nobel[r]
	with open('apis/data/nobel/' + nobel, 'r') as f:
		data = json.load(f)
	return jsonify(data)


@nobel.route('/category')
def get_nobel_by_category():
	cat = request.args.get("category")
	all_nobel = os.listdir('apis/data/nobel/')
	print("categories", cat)
	result = []
	for nobel in all_nobel:
		with open('apis/data/nobel/' + nobel, 'r') as f:
			data = json.load(f)
		print("array", data["category"])
		data_array = data["category"]
		if (cat in data_array):
			result.append(data)
	
	return jsonify(result)

@nobel.route('/docs')
def docs():
	endpoints = [
		{
			'url': '/random',
			'method': 'GET',
			'description': 'Fetch json of any random Nobel Prize winner. Example: nobel/random'
		},
		{
			'url': '/category',
			'method': 'GET',
			'description': 'Fetch Nobel Prize winners of a particular category. Example: nobel/category?category=physics'
		},
	]

	return jsonify({'endpoints': endpoints})
