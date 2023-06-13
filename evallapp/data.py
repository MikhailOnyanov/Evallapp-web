import logging

from flask import (
    Blueprint, render_template, request, current_app, jsonify
)
from sqlalchemy import inspect

from . import db_session
from .models.core import *
from .utils import get_table_by_name

bp = Blueprint('data', __name__, url_prefix='/api')


# returns
@bp.route('/fetch_dataset', methods=['GET'])
def fetch_dataset():
    db_name = request.args.get('db_name')
    if db_name:
        print("privet")
        table_values = get_table_by_name(db_name)
        # r = {
        #     'columns': table_values[0],
        #     'data': [elem.to_dict() for elem in table_values[1]],
        # }
        print(table_values)
        return jsonify(table_values)
    else:
        return "Dataset not found", 400


@bp.route('/data', methods=['GET'])
def data():
    query = db_session.query(Works)
    total = query.count()

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Works.year.like(f'%{search}%'),
            Works.education_profile.like(f'%{search}%')
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        pass
        # order = []
        # for s in sort.split(','):
        #     direction = s[0]
        #     name = s[1:]
        #     if name not in ['name', 'age', 'email']:
        #         name = 'name'
        #     col = getattr(User, name)
        #     if direction == '-':
        #         col = col.desc()
        #     order.append(col)
        # if order:
        #     query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)

    r = {
        'data': [work.to_dict() for work in query],
        'total': total,
    }
    return r
