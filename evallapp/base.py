import logging

from flask import (
    Blueprint, render_template
)
from sqlalchemy import select

from . import db_session
from .models.core import *
from .utils import *

bp = Blueprint('base', __name__)


# @bp.route('/register')
# def register():
#     inf = db_session.execute(select(Works)).scalars()
#     d = inf.all()
#     current_app.logger.info(d)
#     disp = ""
#     for elem in d:
#         disp += str(elem) + "\n"
#     return f'<h1>Testing the Flask Application Factory Pattern, {disp}</h1>'


@bp.route('/base-table')
def base():
    tables = get_database_tables_names() or []
    param2 = ["work_code", "year", "education_profile_number"]
    get_table_by_name("works")
    return render_template('base-table.html', list=tables, param2=param2)
