from flask import Blueprint
from flask_restful import Api
from projectify.blueprints.category.resource.category_resource import CategoryResource

category = Blueprint('category', __name__)
category_api = Api(category)

category_api.add_resource(CategoryResource, '/api/v1/category')
