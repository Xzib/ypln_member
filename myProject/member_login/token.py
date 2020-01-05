from itsdangerous import URLSafeTimedSerializer
from myProject import app


def genrate_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email,salt=app.config['SECRET_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
                    token,
                    salt=app.config['SECRET_PASSWORD_SALT'],
                    max_age=expiration
        )
    except:
        return False
    return email
