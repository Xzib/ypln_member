from flask import Flask
from flask_mail import Mail,Message
import os

mail = Mail()
app = Flask(__name__)

# ###### Form configuration ######
# app.config['SECRET_KEY']= 'mysecretkey'

# ##### Database configuration #####
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#### Email Configuration #####
app.config['MAIL_SERVER'] = 'mail.yplnetwork.com '
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'test@yplnetwork.com'
app.config['MAIL_PASSWORD'] = '1234@1234'
app.config['DEFAULT_MAIL_SENDER'] = None 

mail.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        msg = Message(subject = 'HELLO',
                        sender = 'test@yplnetwork.com',
                        recipients=['syedzohaibali94@hotmail.com'],
                        body = 'test message')
        mail.send(msg)               