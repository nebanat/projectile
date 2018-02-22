from flask import Blueprint
from flask_restful import Api

from projectify.blueprints.user.resources.user_resource import User

user = Blueprint('user', __name__, url_prefix='/user')
user_api = Api(user)

user_api.add_resource(User, '/api')
