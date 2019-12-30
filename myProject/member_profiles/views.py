from flask import Blueprint,redirect,render_template,url_for
from myProject import db
from myProject.models import RegisteredMember, UserInfo

member_profiles_bp = Blueprint('member_profile',__name__,
                                template_folder='templates/member_profiles')



@member_profiles_bp.route('/list')
def list_register_members():
    members = RegisteredMember.query.all()
    return render_template("thankyou.html", members=members)


@member_profiles_bp.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")