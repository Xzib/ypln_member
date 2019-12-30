import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY']= 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

from myProject.member_login.views import member_login_bp
from myProject.member_profiles.views import member_profiles_bp

app.register_blueprint(member_login_bp,url_prefix='/member_login')
app.register_blueprint(member_profiles_bp,url_prefix='/member_profile')