from projectify.models.user import User


# jwt authentication
def authenticate(email, password):
    user = User.filter_by(email=email)
    if user and user.check_password(password):
        return user


# jwt identity
def identity(payload):
    auth_user_id = payload['identity']
    return User.filter_by(id=auth_user_id)
