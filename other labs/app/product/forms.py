from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import Length, InputRequired, DataRequired


class AddProductForm(FlaskForm):
    name = StringField('Name product', validators=[InputRequired(), Length(min=2, max=60)])
    price = StringField('Price', validators=[InputRequired(), Length(min=2, max=60)])
    type = StringField('Type of product', validators=[InputRequired(), Length(min=2, max=60)])
    number = StringField('Number', validators=[InputRequired(), Length(min=2, max=60)])
    date = StringField('Date of receipt', validators=[InputRequired(), Length(min=2, max=60)])
    category = SelectField(u'Category', coerce=int)
    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    name = StringField('Name firm', validators=[DataRequired(), Length(min=0, max=100)])
    submit = SubmitField('')
