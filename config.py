from random import choices
import string
import os


class Config(object):
    TEST = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''.join(choices(string.printable, k=50))
    DEBUG = False
    SESSION_COOKIE_DOMAIN = None    
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')


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