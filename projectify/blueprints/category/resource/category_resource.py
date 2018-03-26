from flask import jsonify
from flask_restful import Resource
from flask_jwt import jwt_required
from webargs.flaskparser import use_args
from projectify.blueprints.category.schemas import CategorySchema
from projectify.models import Category


class CategoryResource(Resource):
    @jwt_required()
    @use_args(CategorySchema, locations=('json', 'form'))
    def post(self, category_args):
        """
         creates a new project category
        :param category_args: category details e.g.name,description
        :return: response with new category details
        """
        checked_category = Category.filter_by(name=category_args['name'])
        if checked_category is not None:
            response = jsonify(dict(status=False,
                                    message='category name already exist'))
            response.status_code = 409
            return response
        else:
            category = Category(**category_args)
            category.save_to_db()
            new_category = CategorySchema().dump(Category.filter_by(id=category.id))
            response = jsonify(dict(status=True,
                                    message='Category created',
                                    data=dict(category=new_category.data)
                                    ))
            response.status_code = 201
            return response
