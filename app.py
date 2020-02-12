from flask import Flask, jsonify, request
import requests

from apis import comics
from apis import test
from apis import nobel

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('config')

# import apis and assigning url_prefix in lexographical order
app.register_blueprint(comics, url_prefix='/api/comics')
app.register_blueprint(nobel, url_prefix='/api/nobel')
app.register_blueprint(test, url_prefix='/api/test')

@app.route('/api')
def api():
    endpoints = ['test', 'comics', 'nobel']
    docs = []
    url = request.url_root
    for endpoint in endpoints:
        data = requests.get('{}api/{}/docs'.format(url, endpoint)).json()
        docs.extend(data['endpoints'])
    return jsonify({'docs': docs})

@app.errorhandler(404)
def error(e):
    return "Use the /api endpoint to get documentation about all the APIs"

if __name__ == "__main__":
    app.run()
