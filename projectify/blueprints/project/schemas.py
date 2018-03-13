from marshmallow import Schema, fields, validate
from core.validation import CustomValidation
from projectify.blueprints.user.schemas import UserSchema


class ProjectSchema(Schema):
    """
    Defines project schema with validations

    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True,
                       validate=[CustomValidation.must_not_be_blank, validate.Length(max=100)],
                       error_messages={'required': 'Project title field is required'})
    description = fields.Str(required=True,
                             validate=[CustomValidation.must_not_be_blank, validate.Length(max=500)],
                             error_messages={'required': 'Project description is required'})
    project_url = fields.URL(required=True,
                             validate=CustomValidation.must_not_be_blank,
                             error_messages={'required': 'Project URL is required'})
    price = fields.Int(required=True,
                       validate=CustomValidation.must_not_be_blank)

    buyout_price = fields.Int(missing=0)

    created_on = fields.DateTime(required=True, dump_only=True)

    updated_on = fields.DateTime(required=True, dump_only=True)

    user = fields.Nested(UserSchema(exclude=("password", "created_on", "updated_on")),
                         validate=CustomValidation.must_not_be_blank)

    class Meta:
        strict = True
        many = True

