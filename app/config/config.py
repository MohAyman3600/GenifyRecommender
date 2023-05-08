import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    TESTING = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    MONGODB_SETTINGS = {
        'host': [os.environ.get('MONGODB_URI')]
    }


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {
        'host': [os.environ.get('MONGODB_URI')]
    }


class ProductionConfig(Config):
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_URI')
    }


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
