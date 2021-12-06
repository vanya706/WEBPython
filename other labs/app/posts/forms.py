from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import Length, InputRequired


class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(min=5, max=120)])
    text = TextAreaField('Text', validators=[Length(max=8000)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    type = SelectField('type',
                       choices=[('Blog', 'Blog'), ('News', 'News'), ('Publication', 'Publication'), ('Other', 'Other'),
                                ('Rss', 'Rss')])
    submit = SubmitField('Submit')
