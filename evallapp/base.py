from flask import (
    Blueprint, render_template
)

from .importers.constants import EXCEL_FILEPATH
from .importers.xlsx.xlsx_operations import ExcelWorker
from .utils import *

# test excel!
from .importers.data_operations import DatabaseCRUD
# test excel!

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



def test_tables():
    # test excel!
    # Прокси объект для работы с БД
    excel_db_proxy = DatabaseCRUD("1")
    current_app.logger.info("Excel started")
    ex = ExcelWorker(EXCEL_FILEPATH)
    print(ex.get_sheets())

    # Добавляет типы ошибок из предопределённого словаря в бд
    # excel_db_proxy.init_mistake_types()

    # получаем коды ошибок из заголовков экселя
    # codes: list[MistakesCodes] = ex.get_mistakes_codes_from_list(7)

    # коды ошибок в БД
    # for elem in codes:
    #     print(elem)
    #     excel_db_proxy.session_add(elem)

    # получаем строки с записями об ошибках
    objects_dataset = ex.process_sheet(7)
    print(objects_dataset)
    # записи об ошибках в бд
    # db_engine.get_mistakes_list()
    if objects_dataset:
        excel_db_proxy.add_sheet_data_to_db(objects_dataset)
    ex.xl.close()
    current_app.logger.info("Finished")
    pass