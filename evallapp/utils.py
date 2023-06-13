from sqlalchemy import inspect, Table, select
from sqlalchemy.orm import DeclarativeMeta

from .models.core import *
from flask import current_app
from .db import engine, db_session, Base

def get_database_tables_names() -> list[str]:
    inspector = inspect(engine)
    schemas = inspector.get_schema_names()
    tables = []
    for schema in schemas:
        if schema != 'information_schema':
            for table_name in inspector.get_table_names(schema=schema):
                tables.append(table_name)
            # for column in inspector.get_columns(table_name, schema=schema):
            # print("Column: %s" % column)
    current_app.logger.info(f"Returned: {tables}")
    return tables


def get_database_views_names() -> list[str]:
    views = []
    inspector = inspect(engine)
    for view_name in inspector.get_view_names():
        if view_name != 'pg_stat_statements':
            views.append(view_name)
    current_app.logger.info(f"Returned: {views}")
    return views


def get_table_by_name(db_name: str) -> list[list[str], list[tuple]]:
    table_class = find_mapper_for_table(Base, db_name)
    res = db_session.scalars(select(table_class)).all()
    if res:
        table_data: list[dict] = []
        table_key: list[str] = list((res[0].to_dict()).keys())

        row_counter = 0

        for val in res:
            row_counter += 1
            obj: dict = val.to_dict()
            table_data.append(obj)

        current_app.logger.info(
            f"Collected {row_counter} rows of '{table_class.__name__}' table."
        )
        return []
    else:
        return []


def find_mapper_for_table(base_class: DeclarativeMeta, target_name: str) -> Base | None:
    d = {}
    for mapper in base_class.registry.mappers:
        cls = mapper.class_
        classname = cls.__name__
        if not classname.startswith('_'):
            table_name = cls.__tablename__
            d[table_name] = cls
    try:
        return d[target_name]
    except KeyError:
        current_app.logger.warning(f"Can't find mapper for {target_name}")
        return None
    except Exception as ex:
        current_app.logger.warning(f"Problems while finding mapper for {target_name}. {ex}")
        return None

"""
table_model: Table = Base.metadata.tables[db_name]
print(table_model)
        print(type(table_model))
        print(res)
columns: list[str] = []

        for column in table_model.columns:
            columns.append(column.key)

        print(columns)

        table_values: list[tuple] = db_session.query(table_model)
        for val in table_values:
            print(val)
            print(type(val))
            break
"""