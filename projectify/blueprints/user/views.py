from flask import Blueprint
from flask_restful import Api

from projectify.blueprints.user.resources.user_resource import UserResource

user = Blueprint('user', __name__)
user_api = Api(user)

user_api.add_resource(UserResource, '/api/v1/register')
