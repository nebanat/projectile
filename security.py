from projectify.blueprints.user.models import User


# jwt authentication
def authenticate(email, password):
    user = User.get_by_email(email)
    if user and user.check_password(password):
        return user


# jwt identity
def identity(payload):
    auth_user_id = payload['identity']
    return User.get_by_id(auth_user_id)
