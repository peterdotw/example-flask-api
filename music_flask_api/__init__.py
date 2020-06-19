from music_flask_api.routes import api
from flask import Flask
from flask_mongoengine import MongoEngine
import os
from dotenv import load_dotenv


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': os.environ['DATABASE_NAME'],
        'host': os.environ['MONGO_URI']
    }
    db = MongoEngine(app)
    app.secret_key = os.environ['SECRET_KEY']
    app.register_blueprint(api)
    return app
