from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

import music_flask_api.routes
