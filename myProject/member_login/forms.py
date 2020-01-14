from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired,InputRequired,EqualTo,Email
from wtforms import ValidationError
from myProject.models import RegisteredMember
from flask_login import current_user


class LoginForm(FlaskForm):
    useremail = StringField("Enter your email", validators=[DataRequired(message="Please enter your email"),Email(message="Invalid email id")],)
    password = PasswordField("Enter your password",validators=[DataRequired(message="Please enter your password")])
 

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
    useremail = StringField("Enter your Username")
    username = StringField("Enter your Username")
    first_name = StringField("Enter your First Name")
    last_name = StringField("Enter your Last Name")
    address = StringField("Enter your address")
    city = StringField("Enter your city")
    country = StringField("Enter your country")
    postal_code = StringField("Enter your postal code")
    about_me  = StringField("Tell people about yourself")
    picture = FileField("Update profile picture", validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField("Update")
    def check_username(self,field):
        if RegisteredMember.query.filter_by(username=field.data).first():
            ValidationError("Your user name has been taken")
    
    def check_email(self, field):
        if RegisteredMember.query.filter_by(useremail=field.data).first():
            ValidationError("Your email has been already registered")

