from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired,InputRequired,EqualTo,Email
from wtforms import ValidationError
from myProject.models import RegisteredMember
from flask_login import current_user


class LoginForm(FlaskForm):
    useremail = StringField("Enter your email", validators=[DataRequired(message="Please enter your email"),Email(message="Please enter a valid email-id")])
    password = PasswordField("Enter your password",validators=[DataRequired()])
 

class SignUpForm(FlaskForm):
    fullname = StringField("Please Enter your full name", validators=[DataRequired()])
    useremail = StringField("Enter your email", validators=[DataRequired(message="Please enter your email"),Email(message="Please enter a valid email-id")])
    username = StringField("Enter a user name",validators=[InputRequired(message="Please enter user name")])
    password = PasswordField("Enter your password",validators=[InputRequired(), EqualTo("repeat_password",message="password must match")])
    repeat_password = PasswordField("re-type password",validators=[DataRequired()])

    def check_email(self, field):
        if RegisteredMember.query.filter_by(useremail=field.data).first():
            ValidationError("Your email has been already registered")
    def check_username(self,field):
        if RegisteredMember.query.filter_by(username=field.data).first():
            ValidationError("Your user name has been taken")
class ProfileForm(FlaskForm):
    useremail = StringField("Enter your Username", validators=[DataRequired()])
    username = StringField("Enter your Username", validators=[DataRequired()])
    first_name = StringField("Enter your First Name", validators=[DataRequired()])
    last_name = StringField("Enter your Last Name", validators=[DataRequired()])
    address = StringField("Enter your address", validators=[DataRequired()])
    city = StringField("Enter your city", validators=[DataRequired()])
    country = StringField("Enter your country", validators=[DataRequired()])
    postal_code = StringField("Enter your postal code", validators=[DataRequired()])
    about_me  = StringField("Tell people about yourself", validators=[DataRequired()])
    picture = FileField("Update profile picture", validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField("Update")
    def check_username(self,field):
        if RegisteredMember.query.filter_by(username=field.data).first():
            ValidationError("Your user name has been taken")
    
    def check_email(self, field):
        if RegisteredMember.query.filter_by(useremail=field.data).first():
            ValidationError("Your email has been already registered")

