from flask import Flask
from projectify.extensions import db
from projectify.blueprints.user.views import user


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

    app.register_blueprint(user)
    extensions(app)

    return app


def extensions(app):
    """
    Register all extensions (mutates the app passed into it)

    :param app:
    :return: None
    """
    db.init_app(app)

    return None
