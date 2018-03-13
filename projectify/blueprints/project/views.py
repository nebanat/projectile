from flask import Blueprint
from flask_restful import Api
from projectify.blueprints.project.resource.project_resource import ProjectResource

project = Blueprint('project', __name__)
project_api = Api(project)


project_api.add_resource(ProjectResource, '/api/v1/project')
