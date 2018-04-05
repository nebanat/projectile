from flask_restful import Resource
from projectify.blueprints.user.schemas import UserSchema
from webargs.flaskparser import use_args
from projectify.models import User


class UserResource(Resource):

    @use_args(UserSchema(), locations=('json', 'form'))
    def post(self, user_args):
        """

        :param user_args: validated user inputs

        Registers and saves the user to database
        :return: newly registered user
        """
        checked_user = User.get_by_username_and_email(user_args['username'], user_args['email'])

        if checked_user is not None:
            if checked_user.username == user_args['username'].lower():
                return dict(message='Username already exist'), 409
            elif checked_user.email == user_args['email']:
                return dict(message='Email already exist'), 409
        else:
            user = User(**user_args)
            user.password = User.encrypt_password(user_args['password'])
            user.save_to_db()
            new_user = UserSchema(exclude=('password',)).dump(User.filter_by(id=user.id))

            return dict(message='User created successfully',
                        data=dict(user=new_user.data)), 201
