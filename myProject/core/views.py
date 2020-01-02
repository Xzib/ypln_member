from flask import Flask, Blueprint, render_template, url_for

core_bp = Blueprint('core',__name__,template_folder='templates/core')

@core_bp.route('/')
def index():
    return render_template('home.html')
 