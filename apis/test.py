from flask import Blueprint, request, jsonify

test = Blueprint('test', __name__)


@test.route('/get')
def get():
    headers = dict(request.headers)
    data = request.args
    return jsonify({
        "headers": headers,
        "data": data,
        "message": "GET request successful"
    })


@test.route('/post', methods=["POST"])
def post():
    headers = dict(request.headers)
    print(headers)
    data = request.get_json()
    return jsonify({
        "headers": headers,
        "data": data,
        "message": "POST request successful"
    })


@test.route('/docs')
def docs():
    endpoints = [
        {
            'url': '/get',
            'method': 'GET',
            'description': 'A test endpoint serving GET requests as a webhook'
        },
        {
            'url': '/post',
            'method': 'POST',
            'description': 'A test endpoint serving POST requests as a webhook'
        }
    ]

    return jsonify({'endpoints': endpoints})
