from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '98a1f4a2b185cd292f408c80d6c4383ba1fa3e69d017dd1b78ade32a5d489be0'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

    from . coffee.url import coffee
    app.register_blueprint(coffee)

    return app
