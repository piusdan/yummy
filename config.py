# -*- coding:utf-8 -*-

"""Configures the application
"""

import os


class Config(object):
    """Base configuration class
    """
    TESTING = False
    DEBUG_MEMCHACHE = False
    SSL_DISABLE = True
    SECRET_KEY = "I\xf9\x9cF\x1e\x04\xe6\xfaF\x8f\xe6)-\xa432"
    CSRF_ENABLED = True


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
