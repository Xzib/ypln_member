##############################################################
###################### Models ################################
#set up db inside the __init__.py file inside myProject dir
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from myProject import db, login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return RegisteredMember.query.get(user_id)

class RegisteredMember(db.Model,UserMixin):
    __tablename__ = 'user_registration'
    '''
    Email confirmation ability
    '''
    id = db.Column(db.Integer, primary_key=True)
    useremail = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    fullname = db.Column(db.Text)
    username = db.Column(db.Text)
    profile_pic = db.Column(db.String(20),nullable=False, default= 'default_profile.png')
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    postal_code = db.Column(db.String, nullable=True)
    about_me = db.Column(db.Text, nullable=True)
    # phone_number = db.Column(db.Integer)
    user_info = db.relationship('UserInfo', backref='registeredmember', uselist = False)

    def __init__(self,fullname, useremail, username, password,
                confirmed,confirmed_on=None,admin=False,first_name=None,
                last_name=None, address = None, city = None, country= None, postal_code= None,
                about_me= None):
        self.fullname = fullname
        self.useremail = useremail
        self.username = username
        self.password = generate_password_hash(password)
        # self.email = email
        # self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.now()
        self.admin = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on

        self.first_name= first_name
        self.last_name= last_name 
        self.address = address  
        self.city = city  
        self.country= country  
        self.postal_code= postal_code 
        self.about_me= about_me 

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

