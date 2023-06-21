from flask import Flask, render_template, Blueprint, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

bp = Blueprint('form', __name__)


# Create Form Class
class MistakeTypeForm(FlaskForm):
    title = StringField("Описание типа ошибки", validators=[DataRequired()])
    submit = SubmitField("Создать")


# Create Type page
@bp.route('/mistake_type', methods=['GET', 'POST'])
def mistake_type():
    title = None
    form = MistakeTypeForm()

    # Validate form
    if form.validate_on_submit():
        title = form.title.data
        form.title.data = ''
        flash("Запись успешно создана!")

    return render_template("form-create-mistake-type.html",
                           title=title,
                           form=form)
