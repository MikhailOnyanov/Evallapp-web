import functools
import logging

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

from .db import db
from .models.core import *

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register')
def register():
    inf = db.session.execute(db.select(Works)).scalars()
    d = inf.all()
    current_app.logger.info(d)
    disp = ""
    for elem in d:
        disp += str(elem) + "\n"
    return f'<h1>Testing the Flask Application Factory Pattern, {disp}</h1>'
