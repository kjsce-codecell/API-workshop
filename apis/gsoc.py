import flask
from flask import request, jsonify, Blueprint


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
<p>A prototype API for giving out random hardcoded GSOC Winners</p><p>Use /winners/all for checking all winners.</p><p>Use /winners?id= for checking a specific winner.</p>'''


@gsoc.route('/winners/all', methods=['GET'])
def api_all():
    return jsonify(winners)


@gsoc.route('/winners', methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = int(request.args['id'])
        # print(len(winners))

    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for winner in winners:
        if winner['id'] == id:
            results.append(winner)

    return jsonify(results)


@gsoc.route('/docs')
def docs():
    endpoints = [
        {
            'url': '/api/gsoc',
            'method': 'GET',
            'description': 'A gsoc endpoint serving GET requests as a webhook'

        },
        {
            'url': '/api/gsoc/winners/all',
            'method': 'GET',
            'description': 'A gsoc endpoint to get list of all gsoc winners'

        },
        {
            'url': '/api/gsoc/winners?id=2',
            'method': 'GET',
            'description': 'A gsoc endpoint to get specific winner'

        },
    ]

    return jsonify({'endpoints': endpoints})
