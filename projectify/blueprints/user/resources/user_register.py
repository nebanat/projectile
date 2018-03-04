# from flask import request
from flask_restful import Resource
from projectify.blueprints.user.schemas import user_register_args
from webargs.flaskparser import use_args
from projectify.blueprints.user.models import User


class UserRegister(Resource):

    @use_args(user_register_args)
    def post(self, user_details=user_register_args):
        """

        :param user_details: validated user inputs

        Registers and saves the user to database
        :return: newly registered user
        """
        checked_user = User.get_by_username_and_email(user_details['username'], user_details['email'])
        if checked_user is not None:
            if checked_user.username == user_details['username'].lower():
                return {'message': 'Username already exist'}, 409
            elif checked_user.email == user_details['email']:
                return {'message': 'Email already exist'}, 409
        else:
            new_user = User(**user_details)
            new_user.password = User.encrypt_password(user_details['password'])
            new_user.save_to_db()
            return {'message': 'User created successfully'}, 201
