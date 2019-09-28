from flask import jsonify, abort, make_response, request
from mongoengine import *
import os

from music_flask_api import app
from music_flask_api.models import Artists

connect(os.environ['DATABASE_NAME'], host = os.environ['MONGO_URI'])

@app.route('/api/music/artists')
def get_artists():
    artists = Artists.objects
    return artists.to_json()

@app.route('/api/music/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    try:
        artist = Artists.objects[artist_id]
        if len(artist) == 0:
            abort(404)
        return artist.to_json()
    except IndexError:
        return abort(404)

@app.route('/api/music/artists', methods=['POST'])
def create_artist():
    if not request.json or not 'name' in request.json:
        abort(400)
    artist = Artists(name = request.json['name'], description = request.json.get('description', '')).save()
    return make_response(jsonify(name = request.json['name'], description = request.json.get('description', '')), 200)

@app.route('/api/music/artists/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    artist = Artists.objects[artist_id]
    if len(artist) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    artist.name = request.json.get('name')
    artist.description = request.json.get('description')
    artist.save()
    return artist.to_json()

@app.route('/api/music/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    artist = Artists.objects[artist_id]
    if len(artist) == 0:
        abort(404)
    artist.delete()
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)