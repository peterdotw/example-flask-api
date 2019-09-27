from music_flask_api import app
from flask import jsonify, abort, make_response, request

artists = [
    {
        'id': 1,
        'name': 'Grimes',
        'description': 'A'
    },
    {
        'id': 2,
        'name': 'Lone',
        'description': 'B'
    },
    {
        'id': 3,
        'name': 'Washed Out',
        'description': "C"
    }
]

@app.route('/api/music/artists')
def get_artists():
    return jsonify({'artists': artists})

@app.route('/api/music/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist = [artist for artist in artists if artist['id'] == artist_id]
    if len(artist) == 0:
        abort(404)
    return jsonify({'artist': artist[0]})

@app.route('/api/music/artists', methods=['POST'])
def create_artist():
    if not request.json or not 'name' in request.json:
        abort(400)
    artist = {
        'id': artists[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    artists.append(artist)
    return jsonify({'artist': artist}), 201

@app.route('/api/music/artists/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    artist = [artist for artist in artists if artist['id'] == artist_id]
    if len(artist) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    artist[0]['name'] = request.json.get('name', artist[0]['name'])
    artist[0]['description'] = request.json.get('description', artist[0]['description'])
    return jsonify({'artist': artist[0]})

@app.route('/api/music/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    artist = [artist for artist in artists if artist['id'] == artist_id]
    if len(artist) == 0:
        abort(404)
    artists.remove(artist[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)