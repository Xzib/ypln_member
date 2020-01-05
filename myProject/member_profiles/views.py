from flask import Blueprint,redirect,render_template,url_for
from myProject import db, mail
from myProject.models import RegisteredMember, UserInfo
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user, login_required,logout_user
from flask import Flask


member_profiles_bp = Blueprint('member_profile',__name__,
                                template_folder='templates/member_profiles')



@member_profiles_bp.route('/list')
@login_required
def list_register_members():
    members = RegisteredMember.query.all()
    return render_template("thankyou.html", members=members)


@member_profiles_bp.route('/thankyou')
@login_required
def thankyou():
    
   
    return render_template("thankyou.html")