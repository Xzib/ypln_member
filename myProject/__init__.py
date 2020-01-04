import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mal import Mail


mail = Mail()
login_manager = LoginManager()

app = Flask(__name__)
###### Form configuration ######
app.config['SECRET_KEY']= 'mysecretkey'

##### Database configuration #####
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#### Email Configuration #####
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = os.environ['EMAIL_USER']
app.config['MAIL_PASSWORD'] = os.environ['EMAIL_PASSWORD']
app.config['DEFAULT_MAIL_SENDER'] = 'zohaib@example.com' 


db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'sign_in'

mail.init_app(app)


from myProject.member_login.views import member_login_bp
from myProject.member_profiles.views import member_profiles_bp
from myProject.core.views import core_bp

app.register_blueprint(core_bp)
app.register_blueprint(member_login_bp,url_prefix='/member_login')
app.register_blueprint(member_profiles_bp,url_prefix='/member_profile')
