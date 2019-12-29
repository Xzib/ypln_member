from flask import Flask,render_template,url_for,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo
from flask_migrate import Migrate
from forms import LoginForm, SignUpForm
import os
basedir  = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)
##############################################################
###################### Models ################################

class RegisteredMember(db.Model):
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
        self.password = password
        # self.phone_number = phone_number
    
    def __repr__(self):
        if self.user_info:
            return f"your username is \'{self.username}\' and your about me is \'{self.user_info.about_me}\' "
        return f"your username is \'{self.username}\' your email is \'{self.useremail}\' your about me is not saved "
    
        

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










# @app.route("/",methods=['GET','POST'])
# def index():
#     username = False
#     password = ""
#     form = LoginForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         form.username.data = ""
#         password = form.password.data
#         form.password.data = ""

#     return render_template("home.html",form=form,username=username,password=password)

@app.route("/")
def index():
    return render_template('home.html')



@app.route("/sign_up",methods = ['GET','POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        fullname = form.fullname.data 
        useremail =  form.useremail.data
        username  = form.username.data
        password  = form.password.data
        member = RegisteredMember(fullname,useremail,username,password)
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('list_register_members'))
    return render_template('signup.html',form=form)
@app.route("/list")
def list_register_members():
    members = RegisteredMember.query.all()
    return render_template("thankyou.html", members=members)

@app.route("/sign_in",methods=['GET','POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        useremail = form.useremail.data
        password = form.password.data
        reg = RegisteredMember.query.filter_by(useremail=useremail).first()
        
        if reg != None:
            if  reg.password == password: 
                return redirect(url_for("thankyou"))
            else:
                return redirect(url_for('sign_in',message = 'Incorrect Password'))
        else:
            return redirect(url_for('sign_in',message = 'Incorrect Email id'))
    return render_template("signin.html",form=form)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

# # @app.route('/username/<name>')
# # def user_latin(name):
# #     name = name.lower()
# #     test_list = []
# #     if name[::-1][0] == 'y':
# #         name = name[:len(name)-1]+"ifus"
# #     else:
# #         name = name[:len(name)-1]+"y"
    
# #     for i in range(10):
# #         test_list.append(name+str(i)) 


# #     return render_template("dashboard.html",name=name, test_list=test_list)



if __name__ == "__main__":
    app.run(debug=True)