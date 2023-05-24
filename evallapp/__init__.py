import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, abort

from flask import Flask
from config import Config
from evallapp.db import init_db


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    init_db(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app


#app = create_app()
#app.run(debug=True)
