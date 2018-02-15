from flask import Flask


def create_app(settings_override=None):
    """
    Creates a new flask application using the factories pattern

    :return: an flask app
    """
    app = Flask(__name__)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    @app.route('/')
    def index():
        return 'Welcome to projectify api'

    return app


