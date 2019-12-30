from flask import Blueprint,render_template,redirect,url_for
from myProject import db
from myProject.models import RegisteredMember
from myProject.member_login.forms import LoginForm, SignUpForm


member_login_bp =  Blueprint('member_login',__name__,
                            template_folder='templates/member_login')

'''
Blueprint for signup form
'''
@member_login_bp.route("/signup",methods=['GET','POST'])
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
        return redirect(url_for('member_profile.list_register_members'))
    return render_template('signup.html',form=form)


'''
Blue print for sign in form
'''

@member_login_bp.route("/sign_in",methods=['GET','POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        useremail = form.useremail.data
        password = form.password.data
        reg = RegisteredMember.query.filter_by(useremail=useremail).first()
        
        if reg != None:
            if  reg.password == password: 
                return redirect(url_for("member_profile.thankyou"))
            else:
                return redirect(url_for('member_login.sign_in',message = 'Incorrect Password'))
        else:
            return redirect(url_for('member_login.sign_in',message = 'Incorrect Email id'))
    return render_template("signin.html",form=form)


