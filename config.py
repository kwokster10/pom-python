import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY =''
    SLACK_CLIENT_ID = os.environ['SLACK_CLIENT_ID']
    SLACK_CLIENT_SECRET = os.environ['SLACK_CLIENT_SECRET']
    SLACK_TOKEN = os.environ['SLACK_TOKEN']

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True