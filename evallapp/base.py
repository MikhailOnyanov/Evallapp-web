from flask import (
    Blueprint, render_template
)
from .utils import *

bp = Blueprint('base', __name__)


@bp.route('/base-table')
def base():
    tables = get_database_tables_names() or []
    return render_template('base-table.html', list=tables)


@bp.route('/query-table')
def query_table():
    views = get_database_views_names() or []
    return render_template('query-table.html', list=views)
