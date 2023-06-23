from flask import Flask, render_template, Blueprint, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from .models.core import *
from .db import db_session

bp = Blueprint('form', __name__)


# Create Form Class
class MistakeTypeForm(FlaskForm):
    title = StringField("Описание типа ошибки", validators=[DataRequired()])
    submit = SubmitField("Создать")


# Create Type page
@bp.route('/mistake_type', methods=['GET', 'POST'])
def mistake_type():
    title = None
    error_flag = False
    form = MistakeTypeForm()

    # Validate form
    if form.validate_on_submit():
        title = form.title.data
        form.title.data = ''
        # Logic for appending data
        try:
            new_mistake_type = MistakesTypes()
            new_mistake_type.mistake_type_transcript = title
            db_session.add(new_mistake_type)
            db_session.commit()
            flash(f"Запись успешно создана: {new_mistake_type} в БД")
        except Exception as ex:
            error_flag = True
            flash(f"Ошибка добавления записи: {ex}")
    print(f"я дошёл до сюда, ef = {error_flag}")
    return render_template("form-create-mistake-type.html",
                           title=title,
                           form=form,
                           error_flag=error_flag)
