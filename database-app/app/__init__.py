from flask import Flask
from app import models, routes
import os


def create_app():
    from . import models, routes
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.sqlite'
    routes.init_app(app)
    return app
