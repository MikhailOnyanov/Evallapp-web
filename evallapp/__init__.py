import os

from .db import init_db, db_session
from flask import Flask
from config import Config
from flask_cors import CORS

def create_app(config_class=Config):

    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)

    # register function for handling db connections
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    # set up db for app
    init_db()

    from . import base
    app.register_blueprint(base.bp)
    from . import data
    app.register_blueprint(data.bp)

    return app

