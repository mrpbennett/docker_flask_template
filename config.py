from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

"""
Instead of a one-size-fits-all config, we can now swap configurations based on which environment Flask is running in. ProdConfig and DevConfig contain values specific to production and development respectively. Both of these classes extend a base class Config which contains values intended to be shared by both. 

Swapping between configs is now this easy:

# app.py

# Using a production configuration
app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.DevConfig')

more info on setting up your config.py:
https://hackersandslackers.com/configure-flask-applications

"""


class Config:
    """Base config."""

    SECRET_KEY = environ.get("SECRET_KEY")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    # DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    # DATABASE_URI = environ.get('DEV_DATABASE_URI')
