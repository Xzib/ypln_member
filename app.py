from flask import Flask,render_template,url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class LoginForm(FlaskForm):
    username = StringField("Enter your name")
    password = StringField("Enter your password")
    submit  =  SubmitField("Sign up")

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
    return render_template("signin.html")



@app.route("/sign_up")
def sign_up():
    return render_template("signup.html")

@app.route("/sign_in",methods=['GET','POST'])
def sign_in():
    form = LoginForm()
    username = None
    password = None
    if form.validate_on_submit():
        nonlocal username, password
        username = form.username.data
        password = form.password.data
    return render_template("thankyou.html",form,)

# @app.route("/thankyou")
# def thankyou():
#     first = request.args.get("first")
#     last = request.args.get("last")
#     return render_template("thankyou.html",first=first, last=last)

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