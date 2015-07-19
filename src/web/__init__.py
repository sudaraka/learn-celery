""" Flask web server module """

from flask import Flask
from celery import Celery

from ..config import Config


celery = Celery(__name__)


def create_app():
    """ Create, initiallize and return the Flask application object """

    app = Flask(__name__)
    app.config.from_object(Config)

    celery.conf.update(app.config)

    from .routes import blueprint
    app.register_blueprint(blueprint, url_prefix='')

    return app
