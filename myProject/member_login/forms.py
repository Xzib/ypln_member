from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired,InputRequired,EqualTo,Email
class LoginForm(FlaskForm):
    useremail = StringField("Enter your email", validators=[DataRequired(message="Please enter your email"),Email(message="Please enter a valid email-id")])
    password = PasswordField("Enter your password",validators=[DataRequired()])
 

class SignUpForm(FlaskForm):
    fullname = StringField("Please Enter your full name", validators=[DataRequired()])
    useremail = StringField("Enter your email", validators=[DataRequired(message="Please enter your email"),Email(message="Please enter a valid email-id")])
    username = StringField("Enter a user name",validators=[InputRequired(message="Please enter user name")])
    password = PasswordField("Enter your password",validators=[InputRequired(), EqualTo("repeat_password",message="password must match")])
    repeat_password = PasswordField("re-type password",validators=[DataRequired()])
   