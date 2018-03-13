from flask import jsonify
from flask_restful import Resource
from webargs.flaskparser import use_args
from projectify.blueprints.project.schemas import ProjectSchema
from projectify.models import Project
from flask_jwt import jwt_required, current_identity


class ProjectResource(Resource):
    @jwt_required()
    @use_args(ProjectSchema(), locations=('json', 'form'))
    def post(self, project_args):
        """
        creates a new project associated to the
        logged in user

        :param project_args: Project details entered by user
        :return: response with newly created project,
        message and status
        """
        project = Project(current_identity.id, **project_args)
        project.save_to_db()
        new_project = ProjectSchema().dump(Project.filter_by(id=project.id))  # serializes response
        response = jsonify(dict(status=True,
                                message='Project created',
                                data=dict(project=new_project.data)
                                ))
        response.status_code = 201
        return response
