import flask
from flask import request, jsonify, Blueprint, abort


gsoc = Blueprint('gsoc', __name__)

winners = [
    {'id': 0,
     'name': 'Korusuke',
     'org': 'Mac Ports',
     'project': 'lorem ipsum',
     'year': '2019'},
    {'id': 1,
     'name': 'inischith',
     'org': 'abra ca dabra',
     'project': 'Implement something',
     'year': '2018'},
    {'id': 2,
     'name': 'Person 3',
     'org': 'Tensorflow',
     'project': 'Poor Mans Rekog',
     'year': '2020'},
    {'id': 3,
     'name': 'CodeCell',
     'org': 'KJSCE',
     'project': 'Competitive Programming.',
     'year': '2015 - Present'},
]


@gsoc.route('/', methods=['GET'])
def home():
    return '''<h1>GSOC Winners</h1>
<p>A prototype API for giving out random hardcoded GSOC Winners</p><p>Use /docs to se how to use the API.</p>'''


@gsoc.route('/winners/all', methods=['GET'])
def api_all():
    return jsonify(winners)


@gsoc.route('/winners/<int:winner_id>', methods=['GET'])
def get_winner(winner_id):
    winner = [winner for winner in winners if winner['id'] == winner_id]
    if len(winner) == 0:
        abort(404)
    return jsonify(winner)


@gsoc.route('/add_winner', methods=['POST'])
def add_winner():
    if not request.json or not 'name' in request.json:
        abort(400)
    student = {
        'id': winners[-1]['id'] + 1,
        'name': request.json['name'],
        'org': request.json.get('org', ""),
        'project': request.json.get('project', ""),
        'year': request.json.get('year', ""),
    }
    winners.append(student)
    return jsonify(winners), 201


@gsoc.route('/winners/<int:winner_id>', methods=['PUT'])
def update_winner(winner_id):
    winner = [winner for winner in winners if winner['id'] ==
              winner_id]  # mentioned id winner is stored in winner[0]
    if len(winner) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'org' in request.json and type(request.json['org']) != str:
        abort(400)
    if 'project' in request.json and type(request.json['project']) != str:
        abort(400)
    if 'year' in request.json and type(request.json['year']) != str:
        abort(400)

    winner[0]['name'] = request.json.get('name', winner[0]['name'])
    winner[0]['org'] = request.json.get(
        'org', winner[0]['org'])
    winner[0]['project'] = request.json.get('project', winner[0]['project'])
    winner[0]['yaer'] = request.json.get('year', winner[0]['year'])
    return jsonify(winner)


@gsoc.route('/winners/<int:winner_id>', methods=['DELETE'])
def delete_winner(winner_id):
    winner = [winner for winner in winners if winner['id'] == winner_id]
    if len(winner) == 0:
        abort(404)
    winners.remove(winner[0])
    return jsonify({'result': True})


@gsoc.route('/docs')
def docs():
    endpoints = [
        {
            'url': '/api/gsoc',
            'method': 'GET',
            'org': 'A gsoc endpoint serving GET requests as a webhook'

        },
        {
            'url': '/api/gsoc/winners/all',
            'method': 'GET',
            'org': 'A gsoc endpoint to get list of all gsoc winners'

        },
        {
            'url': '/api/gsoc/winners/2',
            'method': 'GET',
            'org': 'A gsoc endpoint to get specific winner'

        },
        {
            'url': '/api/gsoc/winners/add_winner',
            'method': 'POST',
            'org': 'A gsoc endpoint to add a new winner'

        },

    ]

    return jsonify({'endpoints': endpoints})
