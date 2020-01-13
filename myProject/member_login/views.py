from flask import Blueprint,render_template,redirect,url_for
from myProject import db
from myProject.models import RegisteredMember, BlogPost
from myProject.member_login.forms import LoginForm, SignUpForm, ProfileForm
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user, login_required,logout_user, current_user
from myProject.member_login.token import genrate_token, confirm_token
from myProject.member_login.email import send_email
from myProject.member_login.decorators import check_confirmed
from myProject.member_login.picture_handler import add_profile_pic
from datetime import datetime


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
                                    password=form.password.data,
                                    confirmed=False)
        db.session.add(member)
        db.session.commit()
        token = genrate_token(member.useremail)
        confirm_url = url_for('.confirm_email', token = token, _external= True)
        html = render_template('confirm_url.html', confirm_url = confirm_url) 
        subject = "Confirm your email"
        send_email(member.useremail,subject,html)
        login_user(member)
        flash("Thank you for Registration, A confirmation email has been sent to you!", "success")
        return redirect(url_for('.unconfirmed'))
    return render_template('signup.html',form=form)

'''
Sign in View
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
                next = url_for('.profile')
            return redirect(next)
    return render_template("signin.html",form=form)


'''
confirm_email view

'''
@member_login_bp.route('/confirm/<token>')  
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired','danger')
    user = RegisteredMember.query.filter_by(useremail=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed, please login', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account', 'success')
    return redirect(url_for('.profile'))

'''
Unconfirmed route

'''

@member_login_bp.route('/unconfirmed')

def unconfirmed():
    if current_user.confirmed:
        return redirect(url_for('core.index'))
    flash('Please confirm your account!', 'warning')
    return render_template('unconfirmed.html')


'''
dashboard
'''
@member_login_bp.route('/profile', methods=['GET','POST'])
@login_required
@check_confirmed
def profile():
    page = request.args.get('page',1,type=int)
    blogposts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template('dashboard.html',blogposts=blogposts)


'''
Resend email 
'''
@member_login_bp.route('/resend')
@login_required
def resend_confirmation():
    token = genrate_token(current_user.useremail)
    confirm_url = url_for('.confirm_email', token = token, _external = True)
    html = render_template('confirm_url.html', confirm_url= confirm_url)
    subject = 'Please confirm your email'
    send_email(current_user.useremail,subject,html)
    flash('A new confirmation email has been sent to you!', 'success')
    return redirect(url_for('.unconfirmed'))

'''
Profile view
'''


@member_login_bp.route('/user_profile', methods = ['GET','POST'])
def user_profile():
    form = ProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data,username)
            current_user.profile_pic = pic
        current_user.username = form.username.data
        current_user.useremail = form.useremail.data
        current_user.first_name = form.first_name.data
        form.last_name.data= form.last_name.data
        current_user.address = form.address.data
        current_user.city = form.city.data
        current_user.country = form.country.data
        current_user.postal_code = form.postal_code.data
        current_user.about_me = form.about_me.data

        db.session.commit()
        flash('User account updated')
        return redirect(url_for('.uesr_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.useremail.data = current_user.useremail
        form.first_name.data = current_user.first_name
        form.last_name.data = form.last_name.data
        form.address.data = current_user.address
        form.city.data = current_user.city
        form.country.data = current_user.country
        form.postal_code.data = current_user.postal_code
        form.about_me.data = current_user.about_me
    profile_image = url_for('static' , filename = 'profile_pics/'+current_user.profile_pic)
    return render_template('user_profile.html', profile_image = profile_image , form = form)




'''
Blog post
'''

@member_login_bp.route("/<username>")
def users_posts(username):
    page = request.args.get('page',1,type=int)
    user = RegisteredMember.query.filter_by(username=username).first_or_404()
    blogposts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template('user_blogs.html',blogposts = blogposts, user=user)


@member_login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you are logged out")
    return redirect(url_for('core.index'))




