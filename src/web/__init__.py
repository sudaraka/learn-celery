""" Flask web server module """

from flask import Flask

from .config import Config


def create_app():
    """ Create, initiallize and return the Flask application object """

    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes import blueprint
    app.register_blueprint(blueprint, url_prefix='')

    return app
