import flask
from flask import jsonify,Blueprint,request,abort

pkmn = Blueprint('pkmn',__name__)

pokemon = [
    {
        'id' : 0,
        'name' : 'Charizard',
        'number' : 6,
        'type1' : 'Fire',
        'type2' : 'Flying',
        'species' : 'Flame Pokemon'
    },

    {
        'id' : 1,
        'name' : 'Pikachu',
        'number' : 25,
        'type1' : 'Electric',
        'type2' : None,
        'species' : 'Mouse Pokemon'
    },

    {
        'id' : 2,
        'name' : 'Gengar',
        'number' : 94,
        'type1' : 'Ghost',
        'type2' : 'Poison',
        'species' : 'Shadow Pokemon',
    },
]

@pkmn.route('/', methods=['GET'])
def home():
    return '''<h1>Pokemon</h1>'''

@pkmn.route('/pokemon/all',methods=['GET'])
def all_pokemon():
    return jsonify(pokemon)

@pkmn.route('/pokemon/<int:dex_number>',methods=['GET'])
def get_pokemon1(dex_number):
    poke = {}
    for p in pokemon:
        if p['number'] == dex_number:
            poke = p
            break
    if len(poke) == 0:
        abort(404)
    return jsonify(poke)

@pkmn.route('/pokemon/<poke_name>',methods=['GET'])
def get_pokemon2(poke_name):
    poke = {}
    for p in pokemon:
        if p['name'].lower() == poke_name.lower():
            poke = p
            break
    if len(poke) == 0:
        abort(404)
    return jsonify(poke)


@pkmn.route('/add',methods=['POST'])
def add_pokemon():
    if not request.json or not 'name' in request.json:
        abort(400)
    poke = {
        'id': pokemon[-1]['id'] + 1,
        'name': request.json['name'],
        'number': request.json.get('number'),
        'type1': request.json.get('type1'),
        'type2': request.json.get('type2',None),
        'species': request.json.get('species', ""),
    }

    pokemon.append(poke)
    return jsonify(pokemon),201

@pkmn.route('/update/<int:pid>',methods=['PUT'])
def update_pokemon(pid):
    poke = {}
    for p in pokemon:
        if p['id'] == pid:
            poke = p
            break
    
    if len(poke) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'number' in request.json and type(request.json['number']) != int:
        abort(400)
    if 'type1' in request.json and type(request.json['type1']) != str:
        abort(400)
    if 'type2' in request.json and type(request.json['type1']) != str:
        abort(400)
    if 'species' in request.json and type(request.json['species']) != str:
        abort(400)
    
    poke['name'] = request.json.get('name', poke['name'])
    poke['number'] = request.json.get('number', poke['number'])
    poke['type1'] = request.json.get('type1', poke['type1'])
    poke['type2'] = request.json.get('type2', poke['type2'])
    poke['species'] = request.json.get('species', poke['species'])
    return jsonify(poke)

@pkmn.route('/delete/<int:pid>',methods=['DELETE'])
def delete_pokemon(pid):
    poke = {}
    for p in pokemon:
        if p['id'] == pid:
            poke = p
            break
    
    if len(poke)==0:
        abort(404)
    pokemon.remove(poke)
    return jsonify({'result': True})

@pkmn.route('/docs')
def docs():
    endpoints = [
        {
            'url': '/api/pkmn',
            'method': 'GET',
            'description': 'A pkmn endpoint serving GET requests as a webhook'

        },
        {
            'url': '/api/pkmn/pokemon/all',
            'method': 'GET',
            'description': 'A pkmn endpoint to get list of all Pokemon'

        },
        {
            'url': '/api/pkmn/pokemon/<int:dex_number>',
            'method': 'GET',
            'description': 'A pkmn endpoint to get specific Pokemon by Pokedex number'

        },
        {
            'url': '/api/pkmn/pokemon/<str:poke_name>',
            'method': 'GET',
            'description': 'A pkmn endpoint to get specific Pokemon by name'

        },
        {
            'url': '/api/pkmn/add',
            'method': 'POST',
            'description': 'A gsoc endpoint to add a new winner'

        },
        {
            'url': '/api/pkmn/update/<int:pid>',
            'method': 'PUT',
            'description': 'A pkmn endpoint to update specific Pokemon details,choose by id'

        },
        {
            'url': '/api/pkmn/delete/<int:pid>',
            'method': 'DELETE',
            'description': 'A pkmn endpoint to delete specific Pokemon,choose by id'

        }

    ]

    return jsonify({'endpoints': endpoints})





    


    



