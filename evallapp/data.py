import logging

from flask import (
    Blueprint, render_template, request, current_app, jsonify, abort, Response
)
from sqlalchemy import inspect

from . import db_session
from .models.core import *
from .utils import get_table_by_name, prepare_columns_gridjs_format, find_mapper_for_table, \
    update_data_for_mapped_table, get_view_by_name

bp = Blueprint('data', __name__, url_prefix='/api')


@bp.route('/fetch_dataset', methods=['GET'])
def fetch_dataset():
    db_name = request.args.get('db_name')
    if db_name:
        table_values = get_table_by_name(db_name, prepare_columns=True)
        return jsonify(table_values)
    else:
        return "Dataset not found", 400


@bp.route('/fetch_view', methods=['GET'])
def fetch_view():
    db_name = request.args.get('db_name')
    if db_name:
        table_values = get_view_by_name(db_name)
        return jsonify(table_values)
    else:
        return "Dataset not found", 400


@bp.route('/data', methods=['POST'])
def update():
    data = request.get_json()
    if 'table_name' not in data:
        abort(400)
    try:
        table_name = data['table_name']
        key = data["id"]
        data_to_change = data['data']
        update_data_for_mapped_table(table_name, key, data_to_change)
        return Response(f"Изменения в '{table_name}' внесены: {key}:{data_to_change}", status=200,
                        mimetype='application/json')
    except Exception as ex:
        return Response(f"Текст ошибки: {ex}", status=500, mimetype='application/json')
