from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextAreaField('Text', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Post')