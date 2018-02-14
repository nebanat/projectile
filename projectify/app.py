from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def index():
        return 'Welcome to projectify api'

    return app


