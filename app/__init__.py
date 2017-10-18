# -*- coding:utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from raven.contrib.flask import Sentry
from flask_login import LoginManager

from config import Config, config

bootstrap = Bootstrap()
sentry = Sentry(
    dsn="https://a88a0c9e894a45bc8a6c3ad872d22c2e:"
        "f5dcef4d47544b62a68b0d0501235366@sentry.io/227387")

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



def create_app(config_name):
    """Application factory to create the application
    :param: config_name - configuration name e.g Development
    :return: app
    :rtype: Flask application instance
    """

    # create flaks instance
    app = Flask(__name__)
    # apply configurations
    app.config.from_object(config[config_name])
    # intialise bootstrap for ui
    bootstrap.init_app(app)
    # intialise sentry for logging 
    sentry.init_app(app, logging=True)
    # initialise session manager
    login_manager.init_app(app)

    # register blueprints
    from app.main import main as main_blueprint


    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    return app