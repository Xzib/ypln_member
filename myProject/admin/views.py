from flask import Blueprint, render_template, redirect, flash, url_for


admin_bp = Blueprint('admin_bp',__name__,template_folder='templates/admin')

@admin_bp.route('/admin ')
def index():
    return render_template('member_login.signin.html')