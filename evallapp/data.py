import logging

from flask import (
    Blueprint, render_template, request, current_app, jsonify, abort
)
from sqlalchemy import inspect

from . import db_session
from .models.core import *
from .utils import get_table_by_name, prepare_columns_gridjs_format, find_mapper_for_table

bp = Blueprint('data', __name__, url_prefix='/api')


@bp.route('/fetch_dataset', methods=['GET'])
def fetch_dataset():
    db_name = request.args.get('db_name')
    if db_name:
        table_values = get_table_by_name(db_name, prepare_columns=True)
        print(table_values)
        return jsonify(table_values)
    else:
        return "Dataset not found", 400


@bp.route('/data', methods=['POST'])
def update():
    data = request.get_json()
    if 'table_name' not in data:
        abort(400)
    print(data)
    t = find_mapper_for_table(Base, data['table_name'])
    mapped_object = db_session.query(t).get(data["id"])
    data_to_change = data['data']
    atr_key = list(data_to_change.keys())[0]
    data_to_write = data_to_change[atr_key]
    setattr(mapped_object, atr_key, data_to_write)
    db_session.commit()


    # user = User.query.get(data['id'])
    #
    # for field in ['name', 'age', 'address', 'phone', 'email']:
    #     if field in data:
    #         setattr(user, field, data[field])
    # db.session.commit()
    return '', 204
