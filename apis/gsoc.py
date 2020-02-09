import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
winners = []


@app.route('/', methods=['GET'])
def home():
    return '''<h1>GSOC Winners</h1>
<p>A prototype API for giving out random hardcoded GSOC Winners</p><p>Use /winners/all for checking all winners.</p>'''


@app.route('/winners/all', methods=['GET'])
def api_all():
    return jsonify(winners)


app.run()
