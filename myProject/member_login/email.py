from flask_mail import Message
from myProject import app, mail

def send_email(to, subject, template):
    msg = Message(subject = subject,    
                    sender =    'test@yplnetwork.com',
                    recipients=[to],
                    html=template)
    mail.send(msg)
