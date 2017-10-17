# -*- coding:utf-8 -*-

"""Configures the application
"""

import os


class Config(object):
    """Base configuration class
    """
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_MEMCHACHE = False
    # sql alchemy conf
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SSL_DISABLE = True
    SECRET_KEY = "I\xf9\x9cF\x1e\x04\xe6\xfaF\x8f\xe6)-\xa432"
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}".format(**{"DB_USER": os.environ.get("DB_USER", 'postgres'),"DB_PASS": os.environ.get("DB_PASS", 'postgres'),"DB_HOST": os.environ.get("DB_HOST", 'localhost'),"DB_NAME": os.environ.get("DB_NAME", 'yummy-recipes')})


class DevelopmentConfig(Config):
    """Development Mode configuration
    """
    DEBUG = True
    CSRF_ENABLED = False

class TestingConfig(Config):
    """Testing mode configuration
    """
    TESTING = True
    CSRF_ENABLED = False


class ProductionConfig(Config):
    """Production Mode configuration
    """
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    
    'default': DevelopmentConfig,
}     
