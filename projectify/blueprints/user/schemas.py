from marshmallow import Schema, fields, validate, pre_load


class UserSchema(Schema):
    """

    Defines User schema with its validation

    """
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=5))
    email = fields.Email(required=True)
    password = fields.Str(required=True,
                          dump_only=False,
                          validate=validate.Length(min=6))

    created_on = fields.DateTime(required=True, dump_only=True)

    updated_on = fields.DateTime(required=True, dump_only=True)

    @pre_load()
    def user_details_to_lower_strip(self, data):
        data['username'] = data['username'].lower().strip()
        data['email'] = data['email'].lower().strip()
        data['password'] = data['password'].strip()
        return data

    class Meta:
        strict = True
        many = True

