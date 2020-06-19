import os
from flask import jsonify, abort, make_response, request, Blueprint
from music_flask_api.models import Artist

api = Blueprint('api', __name__)


@api.route('/api/music/artists')
def get_artists():
    artists = Artist.objects
    return artists.to_json()


@api.route('/api/music/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    try:
        artist = Artist.objects[artist_id]
        if len(artist) == 0:
            abort(404)
        return artist.to_json()
    except IndexError:
        return abort(404)


@api.route('/api/music/artists', methods=['POST'])
def create_artist():
    if not request.json or 'name' not in request.json:
        abort(400)
    artist = Artist(name=request.json['name'], description=request.json.get(
        'description', '')).save()
    return make_response(jsonify(
        name=request.json['name'],
        description=request.json.get('description', '')),
        200)


@api.route('/api/music/artists/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    artist = Artist.objects[artist_id]
    if len(artist) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if ('description' in request.json and
            type(request.json['description']) != str):
        abort(400)
    artist.name = request.json.get('name')
    artist.description = request.json.get('description')
    artist.save()
    return artist.to_json()


@api.route('/api/music/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    artist = Artist.objects[artist_id]
    if len(artist) == 0:
        abort(404)
    artist.delete()
    return jsonify({'result': True})


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@api.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
