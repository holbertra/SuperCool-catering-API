import os

class Config(object):
    DEBUG = False
    TESTING = False

    # dB Connection String
    SQLALCHEMY_DATABASE_URI= os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#    CONNECTION = os.getenv('DATABASE_URI')
    JWT_SECRET_KEY = 'super-secret'  # Change this!
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']

    JWT_SECRET_KEY = os.getenv('SECRET_KEY')

class Development(Config):
    DEBUG = True

class Production(Config):
    pass

class Testing(Config):
    TESTING = True