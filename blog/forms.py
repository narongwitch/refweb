from flask_wtf import FlaskForm
from wtforms import validators, StringField, TextAreaField, SelectField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileAllowed

from blog.models import Category, Goverment

def categories():
    return Category.query


def goverments():
    return Goverment.query

class PostForm(FlaskForm):
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png'], 'We only accept JPG or PNG images')
    ])
    title = StringField('Title', [
            validators.InputRequired(),
            validators.Length(max=80)
        ])
    body = TextAreaField('Content', validators=[validators.InputRequired()])
    category = QuerySelectField('Category', query_factory=categories,
        allow_blank=True)
    new_category = StringField('New Category')

    goverment = QuerySelectField('Goverment', query_factory=goverments,
        allow_blank=True)
    new_goverment = StringField('New Goverment')