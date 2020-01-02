from flask import Blueprint,render_template,redirect,url_for
from myProject import db
from myProject.models import RegisteredMember
from myProject.member_login.forms import LoginForm, SignUpForm
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user, login_required,logout_user


member_login_bp =  Blueprint('member_login',__name__,
                            template_folder='templates/member_login')

'''
Blueprint for signup form
'''
@member_login_bp.route("/signup",methods=['GET','POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        member = RegisteredMember(fullname=form.fullname.data,
                                    useremail=form.useremail.data,
                                    username=form.username.data,
                                    password=form.password.data)
        db.session.add(member)
        db.session.commit()
        flash("Thank you for Registration")

        return redirect(url_for('member_login.sign_in'))
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
        
        if  reg.check_password(password) and reg is not None: 
            login_user(reg)
            flash('logged in Successfully')
            next = request.args.get('next')
            if (next == None) or (not next[0] == "/"):
                next = url_for('member_profile.thankyou')
            return redirect(next)
    return render_template("signin.html",form=form)

@member_login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you are logged out")
    return redirect(url_for('core.index'))

