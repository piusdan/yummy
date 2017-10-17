# -*- coding:utf-8 -*-

from flask import Flask
from celery import Celery
from raven.contrib.flask import Sentry

from app.config import config, Config


sentry = Sentry(
    dsn="https://a88a0c9e894a45bc8a6c3ad872d22c2e:"
        "f5dcef4d47544b62a68b0d0501235366@sentry.io/227387")


def create_app(config_name):
    """Application factory to create the application
    :param: config_name - configuration name e.g Development
    :return: app
    :rtype: Flask application instance
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    
    sentry.init_app(app, logging=True)

    # register blueprints
    from app.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app