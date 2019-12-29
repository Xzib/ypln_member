from flask import Flask,render_template,url_for,request,redirect,session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class LoginForm(FlaskForm):
    useremail = StringField("Enter your email", validators=[DataRequired(message="Please enter your email"),Email(message="Please enter a valid email-id")])
    password = PasswordField("Enter your password",validators=[DataRequired()])
    submit  =  SubmitField("Sign up")

class SignUpForm(FlaskForm):
    fullname = StringField("Please Enter your full name", validators=[DataRequired()])
    useremail = StringField("Enter your email", validators=[DataRequired(message="Please enter your email"),Email(message="Please enter a valid email-id")])
    username = StringField("Enter a user name",validators=[InputRequired(message="Please enter user name")])
    password = PasswordField("Enter your password",validators=[InputRequired(), EqualTo("repeat_password",message="password must match")])
    repeat_password = PasswordField("re-type password",validators=[DataRequired()])
    signup = SubmitField("Sign up")
    signin = SubmitField("Sign in")


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



@app.route("/sign_up")
def sign_up():
    return render_template("signup.html")

@app.route("/sign_in",methods=['GET','POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        
        session['useremail'] = form.useremail.data
        session['password'] = form.password.data
        
        return redirect(url_for("thankyou"))
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