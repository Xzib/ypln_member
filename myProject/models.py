##############################################################
###################### Models ################################
#set up db inside the __init__.py file inside myProject dir
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from myProject import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return RegisteredMember.query.get(user_id)

class RegisteredMember(db.Model,UserMixin):
    __tablename__ = 'user_registration'
    
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.Text)
    useremail = db.Column(db.Text)
    username = db.Column(db.Text)   
    password = db.Column(db.Text)
    # phone_number = db.Column(db.Integer)
    user_info = db.relationship('UserInfo', backref='registeredmember', uselist = False)

    def __init__(self,fullname, useremail, username, password):
        self.fullname = fullname
        self.useremail = useremail
        self.username = username
        self.password = generate_password_hash(password)
        # self.phone_number = phone_number
    
    def check_password(self, password):
        return check_password_hash(self.password,password)
    # def __repr__(self):
    #     if self.user_info:
    #         return f"your username is \'{self.username}\' and your about me is \'{self.user_info.about_me}\' "
    #     return f"your username is \'{self.username}\' your email is \'{self.useremail}\' your about me is not saved "
    
        

class UserInfo(db.Model):

    __tablename__ = "user_info"
    id = db.Column(db.Integer,primary_key=True)
    about_me = db.Column(db.Text)
    registered_member_id = db.Column(db.Integer,db.ForeignKey('user_registration.id'))

    def __init__(self,about_me,registered_member_id):
        self.about_me=about_me
        self.registered_member_id= registered_member_id
    
    def __repr__(self):
        return f"hi {self.about_me}"

