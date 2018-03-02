from flask import Blueprint
from flask_restful import Api

from projectify.blueprints.user.resources.user_register import UserRegister

user = Blueprint('user', __name__)
user_api = Api(user)

user_api.add_resource(UserRegister, '/api/v1/register')
