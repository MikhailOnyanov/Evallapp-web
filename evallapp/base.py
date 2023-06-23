from flask import (
    Blueprint, render_template
)
from .utils import *

bp = Blueprint('base', __name__)


@bp.route('/base-tables-page')
def base():
    tables = get_database_tables_names() or []
    return render_template('base-tables-page.html', list=tables)


@bp.route('/view-queries-page')
def query_table():
    views = get_database_views_names() or []
    return render_template('view-queries-page.html', list=views)

@bp.route('/charts')
def charts():
    views = get_database_views_names() or []
    return render_template('charts-and-diagrams-page.html', list=views)
