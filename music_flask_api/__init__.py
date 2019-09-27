from flask import Flask

app = Flask(__name__)

import music_flask_api.routes
