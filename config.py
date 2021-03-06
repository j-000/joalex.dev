from random import choices
import string


class Config(object):
    TEST = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''.join(choices(string.printable, k=50))
    DEBUG = False
    SESSION_COOKIE_DOMAIN = 'localhost.localdomain'    

class ProdConfig(Config):
    ENV = 'production'
    SERVER_NAME = 'joalex.dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'

class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    TEST = True
    SERVER_NAME = '127.0.0.1:5000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'